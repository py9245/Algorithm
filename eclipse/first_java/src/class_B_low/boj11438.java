package class_B_low;

import java.io.*;
import java.util.*;

public class boj11438{

    static int N, M;
    static int K; // 2^K승 까지의 부모를 저장할 깊이 (N=10만이면 K=17~18 정도면 충분)
    
    // depth[i]: i번 노드의 깊이 (루트는 1부터 시작한다고 가정)
    static int[] depth;
    
    // parent[k][v]: 노드 v의 2^k번째 조상 번호
    // 예: parent[0][3] -> 3번 노드의 2^0(1)번째 조상 (바로 위 부모)
    // 예: parent[3][5] -> 5번 노드의 2^3(8)번째 조상
    static int[][] parent;
    
    // 양방향 그래프 정보 저장 (입력 단계에선 누가 부모인지 모르니까)
    static ArrayList<Integer>[] adj;

    public static void main(String[] args) throws Exception {
         System.setIn(new FileInputStream("res/class_B_low/11438.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        // 1. K값(최대 높이) 구하기
        // N이 10만일 때, 2^17 > 100,000 이므로 K=18이면 충분함
        K = 0;
        int tempN = 1;
        while (tempN <= N) {
            tempN *= 2;
            K++;
        }

        // 2. 초기화
        depth = new int[N + 1];
        parent = new int[K][N + 1]; // 행: 2^k 점프, 열: 노드 번호
        adj = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        // 3. 트리 연결 정보 입력 (양방향)
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj[a].add(b);
            adj[b].add(a);
        }

        // ---------------------------------------------------------
        // [Step 1] 트리 만들기 & 기본 부모(1칸 위) 찾기
        // ---------------------------------------------------------
        bfs(1); 

        // ---------------------------------------------------------
        // [Step 2] 희소 배열(Sparse Table) 채우기 (DP)
        // 공식: 내 2^k번째 조상은 = (내 2^(k-1)번째 조상)의 -> 2^(k-1)번째 조상이다.
        // 의미: 8칸 위로 가고 싶으면? -> 4칸 올라간 뒤, 거기서 또 4칸 올라가면 된다.
        // ---------------------------------------------------------
        for (int k = 1; k < K; k++) { // k: 점프 크기 지수 (1부터 시작, 0은 BFS에서 채움)
            for (int node = 1; node <= N; node++) {
                // intermediate: 중간 기착지 (내 2^(k-1)번째 조상)
                int intermediate = parent[k - 1][node];
                
                // 중간 기착지가 존재하면, 거기서 한 번 더 점프
                if (intermediate != 0) {
                    parent[k][node] = parent[k - 1][intermediate];
                }
            }
        }

        // ---------------------------------------------------------
        // [Step 3] LCA 쿼리 처리
        // ---------------------------------------------------------
        M = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            sb.append(lca(a, b)).append('\n');
        }
        
        System.out.println(sb);
    }

    // BFS: 1번 루트부터 내려가면서 깊이(depth)와 바로 위 부모(parent[0])를 기록
    static void bfs(int root) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(root);
        
        depth[root] = 1; // 루트 깊이는 1로 설정 (방문 체크 겸용)
        
        while (!q.isEmpty()) {
            int curr = q.poll();
            
            for (int next : adj[curr]) {
                // depth가 0이면 아직 방문 안 한 것 (즉, next가 자식임)
                if (depth[next] == 0) {
                    depth[next] = depth[curr] + 1; // 깊이 기록
                    parent[0][next] = curr;        // 바로 위 부모(2^0) 기록
                    q.add(next);
                }
            }
        }
    }

    // LCA: 두 노드의 최소 공통 조상 찾기
    static int lca(int a, int b) {
        // 1. 무조건 b가 더 깊은 녀석이 되도록 스왑 (구현 편의상)
        if (depth[a] > depth[b]) {
            int temp = a;
            a = b;
            b = temp;
        }

        // 2. 키 맞추기 (Deep한 b를 a 높이까지 올림)
        // 큰 점프(K-1)부터 시도하면서 내려옴
        for (int k = K - 1; k >= 0; k--) {
            // b가 2^k만큼 점프해도 a보다 깊거나 같으면 점프! (a 위로 넘어가면 안 됨)
            // depth[a] <= depth[parent[k][b]] 의 의미:
            // "점프한 곳(parent[k][b])의 깊이가 아직 a보다 밑에 있니?"
            if (depth[b] - depth[a] >= (1 << k)) { 
                // 위 조건은 (depth[parent[k][b]] >= depth[a]) 와 같은 의미인데 더 직관적인 비트 연산 방식
                b = parent[k][b];
            }
        }

        // 키를 맞췄는데 둘이 같다면? (애초에 부모-자식 관계였음)
        if (a == b) return a;

        // 3. 같이 점프하기 (공통 조상 바로 밑까지)
        // 둘이 다르다면 계속 위로 점프. 단, "같아지는 지점"으로는 점프 안 함(지나친 거니까)
        for (int k = K - 1; k >= 0; k--) {
            if (parent[k][a] != parent[k][b]) {
                a = parent[k][a];
                b = parent[k][b];
            }
        }

        // 4. 반복문이 끝나면 a와 b는 "공통 조상 바로 아래"에 있음
        // 따라서 a의 바로 위 부모가 정답
        return parent[0][a];
    }
}