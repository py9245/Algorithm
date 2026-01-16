package class_B_low;

import java.io.*;
import java.util.*;

public class boj2042 {
    static int N, M, K;
    static long[] tree;
    static int S; // 리프 노드 시작 인덱스

    public static void main(String[] args) throws Exception {
    	System.setIn(new FileInputStream("res/class_B_low/input2042.txt"));;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 1. S 구하기 (Leaf Node 시작점 & Offset)
        S = 1;
        while (S < N) {
            S *= 2;
        }

        // 2. 트리 생성 및 초기값 입력
        tree = new long[S * 2]; // 0번 인덱스 안 씀
        for (int i = 0; i < N; i++) {
            tree[S + i] = Long.parseLong(br.readLine());
        }

        // 3. Build (내부 노드 채우기)
        for (int i = S - 1; i > 0; i--) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }

        // 4. 명령 처리
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) { // 값 변경
                update(b, c);
            } else { // 구간 합
                sb.append(query(b, (int)c)).append("\n");
            }
        }
        System.out.println(sb);
    }

    static void update(int targetIndex, long val) {
        // Leaf 노드 인덱스로 변환
        int node = S + targetIndex - 1;
        tree[node] = val; // 값 갱신

        // 부모로 올라가며 갱신
        node /= 2;
        while (node > 0) {
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
            node /= 2;
        }
    }

    static long query(int left, int right) {
        int l = S + left - 1;
        int r = S + right - 1;
        long sum = 0;

        while (l <= r) {
            if (l % 2 == 1) sum += tree[l++]; // 왼쪽 경계가 홀수(오른쪽 자식)면 선택 후 안쪽 이동
            if (r % 2 == 0) sum += tree[r--]; // 오른쪽 경계가 짝수(왼쪽 자식)면 선택 후 안쪽 이동
            l /= 2;
            r /= 2;
        }
        return sum;
    }
}