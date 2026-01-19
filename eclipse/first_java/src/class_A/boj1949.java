package class_A;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj1949 {

    static int N;
    static int[] people;
    // 아예 따로 만드니 훨씬 보기 좋죠?
    static int[] dpSelected;    // 내가 우수 마을일 때 (bestdp)
    static int[] dpUnselected;  // 내가 우수 마을이 아닐 때 (worstdp)
    static ArrayList<Integer>[] node;

    // DFS (Bottom-Up 방식)
    static void dfs(int cur, int parent) {
        // 1. 초기값 설정
        dpSelected[cur] = people[cur]; // 선정되면 내 인구수 획득
        dpUnselected[cur] = 0;         // 선정 안 되면 0부터 시작

        // 2. 자식 노드 탐색
        for (int child : node[cur]) {
            if (child == parent) continue; // 부모로 역주행 방지

            dfs(child, cur); // 자식 먼저 계산하고 와라 (재귀)

            // 3. 점화식 적용
            // 내가 '선정'됨 -> 자식은 무조건 '미선정'이어야 함 (인접 불가)
            dpSelected[cur] += dpUnselected[child];

            // 내가 '미선정' -> 자식은 '선정'되든 말든 더 이득인 걸로 가져옴
            dpUnselected[cur] += Math.max(dpSelected[child], dpUnselected[child]);
        }
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("res/class_A/1949.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        people = new int[N + 1];
        dpSelected = new int[N + 1];
        dpUnselected = new int[N + 1];
        node = new ArrayList[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            people[i] = Integer.parseInt(st.nextToken());
            node[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            node[a].add(b);
            node[b].add(a);
        }

        // 1번 마을부터 루트로 잡고 시작 (부모는 없으니 -1 또는 0)
        dfs(1, 0);

        // 1번 마을이 선정됐을 때 vs 안 됐을 때 중 최대값 출력
        System.out.println(Math.max(dpSelected[1], dpUnselected[1]));
    }
}