package class_B.파일공유;

import java.util.*;

class UserSolution {

    // --- 1. 자료구조 정의 ---
    static final int INF = Integer.MAX_VALUE;
    static final int MAX_DIST = 5000;
    static final int MAX_NODE = 1001;

    // 요청 상태 객체
    static class Request {
        int uId;
        int fId;
        int totalSize;
        long downloaded;
        int speed;
        boolean isDone;
        // [최적화] 내가 현재 이 파일을 받고 있는 소스 컴퓨터들의 목록 (중복 방지 & 증분 업데이트용)
        boolean[] connectedSources; 

        public Request(int uId, int fId, int totalSize) {
            this.uId = uId;
            this.fId = fId;
            this.totalSize = totalSize;
            this.downloaded = 0;
            this.speed = 0;
            this.isDone = false;
            this.connectedSources = new boolean[MAX_NODE];
        }
    }

    static class Edge implements Comparable<Edge> {
        int node, weight;
        public Edge(int node, int weight) { this.node = node; this.weight = weight; }
        @Override
        public int compareTo(Edge o) { return this.weight - o.weight; }
    }

    // 전역 변수
    static int N;
    static int lastTime;
    static ArrayList<Edge>[] adjList;
    static ArrayList<Request> activeRequests; // 전체 활성 요청 (update용)
    static ArrayList<Request>[] requestsByUser; // 유저별 요청 (addLink 최적화용)
    
    // 파일 정보 (0:공유소스, 1:보유현황)
    static HashMap<Integer, Integer>[][] files;
    static int[] globalFileSize;

    // --- 2. 메모리 최적화용 전역 객체 (GC 방지) ---
    static int[] dist = new int[MAX_NODE];
    static boolean[] visited = new boolean[MAX_NODE]; // addLink 영향권 찾기용
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public void init(int N, int mShareFileCnt[], int mFileID[][], int mFileSize[][]) {
        this.N = N;
        this.lastTime = 0;
        
        adjList = new ArrayList[N + 1];
        activeRequests = new ArrayList<>();
        requestsByUser = new ArrayList[N + 1];
        files = new HashMap[2][N + 1];
        globalFileSize = new int[1000001];

        for (int i = 0; i <= N; i++) {
            adjList[i] = new ArrayList<>();
            requestsByUser[i] = new ArrayList<>();
            files[0][i] = new HashMap<>();
            files[1][i] = new HashMap<>();
        }

        for (int i = 0; i < N; i++) {
            int uId = i + 1;
            for (int j = 0; j < mShareFileCnt[i]; j++) {
                int fId = mFileID[i][j];
                int size = mFileSize[i][j];
                globalFileSize[fId] = size;
                files[0][uId].put(fId, size);
                files[1][uId].put(fId, size);
            }
        }
    }

    public void makeNet(int K, int mComA[], int mComB[], int mDis[]) {
        for (int i = 0; i < K; i++) {
            int u = mComA[i];
            int v = mComB[i];
            int w = mDis[i];
            adjList[u].add(new Edge(v, w));
            adjList[v].add(new Edge(u, w));
        }
    }

    void update(int mTime) {
        int gap = mTime - lastTime;
        if (gap > 0) {
            // [최적화] iterator 사용 (삭제가 빈번하지 않으므로 일반 for문도 OK)
            for (Request req : activeRequests) {
                if (req.isDone) continue;

                req.downloaded += (long) gap * req.speed;
                if (req.downloaded >= req.totalSize) {
                    req.downloaded = req.totalSize;
                    req.isDone = true;
                }
                files[1][req.uId].put(req.fId, (int)req.downloaded);
            }
        }
        lastTime = mTime;
    }

    public void addLink(int mTime, int mComA, int mComB, int mDis) {
        update(mTime);

        adjList[mComA].add(new Edge(mComB, mDis));
        adjList[mComB].add(new Edge(mComA, mDis));

        // [최적화 2] 링크 양 끝점에서 5000 이내에 있는 '유저들'만 찾아서 재계산
        // 전체 activeRequests를 도는 것보다 훨씬 빠름
        findAffectedAndRefresh(mComA, mComB);
    }

    public void addShareFile(int mTime, int mComA, int mFileID, int mSize) {
        update(mTime);
        
        globalFileSize[mFileID] = mSize;
        files[0][mComA].put(mFileID, mSize);
        files[1][mComA].put(mFileID, mSize);

        // [최적화 1] 역발상: 이 파일을 필요로 하는 주변 놈들을 찾아가서 속도 올려줌
        propagateNewFile(mComA, mFileID);
    }

    public int downloadFile(int mTime, int mComA, int mFileID) {
        update(mTime);

        int size = globalFileSize[mFileID];
        Request req = new Request(mComA, mFileID, size);
        
        // 처음엔 전체 계산 (어쩔 수 없음)
        calcSpeed(req);
        
        activeRequests.add(req);
        requestsByUser[mComA].add(req); // 유저별 관리
        files[1][mComA].put(mFileID, 0);

        return req.speed / 9;
    }

    public int getFileSize(int mTime, int mComA, int mFileID) {
        update(mTime);
        return files[1][mComA].getOrDefault(mFileID, 0);
    }

    // --- 3. 로직 함수들 (핵심) ---

    // [최적화 1 구현] 새 파일 소스(startNode)로부터 5000 이내 유저들에게 알림
    void propagateNewFile(int startNode, int fId) {
        pq.clear();
        Arrays.fill(dist, INF);
        
        dist[startNode] = 0;
        pq.add(new Edge(startNode, 0));

        while (!pq.isEmpty()) {
            Edge curr = pq.poll();
            if (curr.weight > dist[curr.node]) continue;
            if (curr.weight > MAX_DIST) continue;

            // 현재 노드(curr.node)가 이 파일을 요청 중인가?
            for (Request req : requestsByUser[curr.node]) {
                // 완료되지 않았고, 파일ID가 일치하며, 아직 이 소스에서 안 받고 있다면
                if (!req.isDone && req.fId == fId && !req.connectedSources[startNode]) {
                    req.connectedSources[startNode] = true;
                    req.speed += 9;
                }
            }

            for (Edge next : adjList[curr.node]) {
                int nextDist = curr.weight + next.weight;
                if (nextDist <= MAX_DIST && nextDist < dist[next.node]) {
                    dist[next.node] = nextDist;
                    pq.add(new Edge(next.node, nextDist));
                }
            }
        }
    }

    // [최적화 2 구현] 링크 추가 시 영향 받는 유저 찾기
    void findAffectedAndRefresh(int nodeA, int nodeB) {
        // A와 B에서 각각 5000 이내에 있는 모든 노드를 찾음 (Visited 배열로 합집합 처리)
        // BFS/다익스트라 둘 다 가능하나, 거리 계산이 필요하므로 다익스트라 재사용
        // 여기서는 단순히 '도달 가능한 유저'만 찾으면 됨
        
        Arrays.fill(visited, false);
        checkReachability(nodeA);
        checkReachability(nodeB);

        // 영향권에 있는 유저들의 요청만 재계산
        for (int i = 1; i <= N; i++) {
            if (visited[i]) {
                for (Request req : requestsByUser[i]) {
                    if (!req.isDone) {
                        calcSpeed(req); // 얘는 어쩔 수 없이 풀스캔 다시 해야 함 (경로가 짧아졌을 수 있으므로)
                    }
                }
            }
        }
    }

    void checkReachability(int startNode) {
        pq.clear();
        Arrays.fill(dist, INF);
        dist[startNode] = 0;
        pq.add(new Edge(startNode, 0));

        while (!pq.isEmpty()) {
            Edge curr = pq.poll();
            if (curr.weight > dist[curr.node]) continue;
            if (curr.weight > MAX_DIST) continue;

            visited[curr.node] = true; // 방문 체크 (영향권)

            for (Edge next : adjList[curr.node]) {
                int nextDist = curr.weight + next.weight;
                if (nextDist <= MAX_DIST && nextDist < dist[next.node]) {
                    dist[next.node] = nextDist;
                    pq.add(new Edge(next.node, nextDist));
                }
            }
        }
    }

    // 요청 하나에 대해 처음부터 속도 계산 (connectedSources 배열 채우기)
    void calcSpeed(Request req) {
        pq.clear();
        Arrays.fill(dist, INF);
        
        // 초기화
        req.speed = 0;
        Arrays.fill(req.connectedSources, false);

        dist[req.uId] = 0;
        pq.add(new Edge(req.uId, 0));
        
        int sourceCount = 0;

        while (!pq.isEmpty()) {
            Edge curr = pq.poll();
            if (curr.weight > dist[curr.node]) continue;
            if (curr.weight > MAX_DIST) continue;

            // 파일 가지고 있는지 확인
            if (curr.node != req.uId && files[0][curr.node].containsKey(req.fId)) {
                // 중복 체크 없이, 다익스트라 경로상 처음 만나면 유효
                // 하지만 다익스트라는 모든 노드를 방문하므로, 여기서 그냥 체크하면 됨
                // files[0] 확인만 하면 됨. 
                // 단, connectedSources 갱신
                if (!req.connectedSources[curr.node]) {
                    req.connectedSources[curr.node] = true;
                    sourceCount++;
                }
            }

            for (Edge next : adjList[curr.node]) {
                int nextDist = curr.weight + next.weight;
                if (nextDist <= MAX_DIST && nextDist < dist[next.node]) {
                    dist[next.node] = nextDist;
                    pq.add(new Edge(next.node, nextDist));
                }
            }
        }
        req.speed = sourceCount * 9;
    }
}