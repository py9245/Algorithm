package class_B_low;

import java.io.*;
import java.util.*;

public class boj3176 {

    static int N, log, Q;
    static final long INF = Long.MAX_VALUE; // 초기화용 큰 값
    static int[] depth;
    static long[][] minDist, maxDist; // 희소 배열: [k][v] -> v에서 2^k번째 부모까지 가는 길의 최소/최대
    static int[][] parent; // 희소 배열: [k][v] -> v의 2^k번째 부모 노드 번호

    static class Edge implements Comparable<Edge> {
        int node;
        long cost;

        public Edge(int node, long cost) {
            this.node = node;
            this.cost = cost;
        }

        public int compareTo(Edge o) {
            return (int) (this.cost - o.cost);
        }
    }

    static ArrayList<Edge>[] node;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("res/class_B_low/3176.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        depth = new int[N + 1];
        node = new ArrayList[N + 1];

        // 1. Log값 계산 (최대 깊이에 따른 희소 배열 크기 결정)
        log = 0;
        int temp = 1;
        while (temp <= N) {
            temp *= 2;
            ++log;
        }

        // 2. 배열 초기화
        minDist = new long[log][N + 1];
        maxDist = new long[log][N + 1];
        parent = new int[log][N + 1];

        // minDist는 최솟값을 구해야 하므로 INF로 초기화
        for (int i = 0; i < log; i++) {
            Arrays.fill(minDist[i], INF);
        }
        // maxDist는 0으로 초기화 (자바 기본값이므로 생략 가능하나 명시적 표현)

        for (int i = 0; i < N + 1; i++) {
            node[i] = new ArrayList<Edge>();
        }

        StringTokenizer st;
        int a, b, c;

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            node[a].add(new Edge(b, c));
            node[b].add(new Edge(a, c));
        }

        // 3. BFS를 통한 트리 구성 (Depth, Parent[0], 1칸 거리 min/max 계산)
        Deque<Edge> deque = new ArrayDeque<>();
        
        // 1번 노드를 루트로 가정
        deque.add(new Edge(1, 0));
        depth[1] = 0;
        
        boolean[] visi = new boolean[N + 1];
        visi[1] = true; // 루트 방문 처리

        while (!deque.isEmpty()) {
            Edge curr = deque.poll();
            
            for (Edge next : node[curr.node]) {
                if (visi[next.node]) continue;
                
                visi[next.node] = true;
                depth[next.node] = depth[curr.node] + 1;
                
                // 바로 위 부모(2^0 = 1번째 조상) 정보 저장
                parent[0][next.node] = curr.node;
                minDist[0][next.node] = next.cost;
                maxDist[0][next.node] = next.cost;
                
                deque.add(next);
            }
        }

        // 4. 희소 배열(Sparse Table) 완성하기 (DP)
        // 점화식: 2^i번째 조상 = (2^(i-1)번째 조상)의 2^(i-1)번째 조상
        for (int i = 1; i < log; i++) {
            for (int j = 1; j < N + 1; j++) {
                int p = parent[i - 1][j]; // 중간 지점 (2^(i-1)번째 조상)
                
                if (p != 0) {
                    parent[i][j] = parent[i - 1][p];
                    
                    // 경로상의 최솟값: (나~중간) 최솟값 vs (중간~목적지) 최솟값
                    minDist[i][j] = Math.min(minDist[i - 1][j], minDist[i - 1][p]);
                    
                    // 경로상의 최댓값: (나~중간) 최댓값 vs (중간~목적지) 최댓값
                    maxDist[i][j] = Math.max(maxDist[i - 1][j], maxDist[i - 1][p]);
                }
            }
        }

        // 5. LCA 쿼리 처리
        Q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder(); // 출력 성능을 위해 StringBuilder 사용 필수

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            // 항상 b가 더 깊은 노드가 되도록 스왑
            if (depth[a] > depth[b]) {
                int tempNum = a;
                a = b;
                b = tempNum;
            }

            long minEdge = INF;
            long maxEdge = 0;

            // Step 1: 깊이 맞추기 (b를 끌어올림)
            // diff의 비트를 확인하여 필요한 만큼 점프 (BOJ 3117과 동일 원리)
            for (int j = log - 1; j >= 0; j--) {
                if ((depth[b] - depth[a]) >= (1 << j)) { 
                    // 점프하면서 해당 구간의 min/max 갱신
                    minEdge = Math.min(minEdge, minDist[j][b]);
                    maxEdge = Math.max(maxEdge, maxDist[j][b]);
                    
                    b = parent[j][b]; // b를 부모로 이동
                }
            }

            // Step 2: 공통 조상 찾기 (둘 다 같이 끌어올림)
            if (a != b) {
                // 루트 바로 아래까지만 이동 (LCA 직전까지)
                for (int j = log - 1; j >= 0; j--) {
                    if (parent[j][a] != parent[j][b]) {
                        // a쪽 경로 갱신
                        minEdge = Math.min(minEdge, minDist[j][a]);
                        maxEdge = Math.max(maxEdge, maxDist[j][a]);
                        
                        // b쪽 경로 갱신
                        minEdge = Math.min(minEdge, minDist[j][b]);
                        maxEdge = Math.max(maxEdge, maxDist[j][b]);

                        // 두 노드 모두 위로 이동
                        a = parent[j][a];
                        b = parent[j][b];
                    }
                }
                
                // Step 3: 마지막 연결 (LCA 도달)
                // 위 루프가 끝나면 a와 b는 LCA 바로 밑에 있음.
                // 따라서 바로 위 부모(parent[0])로 가는 간선까지 체크해야 함.
                minEdge = Math.min(minEdge, minDist[0][a]);
                minEdge = Math.min(minEdge, minDist[0][b]); // 반대쪽도
                
                maxEdge = Math.max(maxEdge, maxDist[0][a]);
                maxEdge = Math.max(maxEdge, maxDist[0][b]);
            }

            sb.append(minEdge).append(" ").append(maxEdge).append("\n");
        }
        
        System.out.println(sb);
    }
}