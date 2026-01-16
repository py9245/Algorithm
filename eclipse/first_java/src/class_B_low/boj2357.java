package class_B_low;

import java.io.*;
import java.util.*;

public class boj2357 {

    static int N, M;
    static int[] minTree; 
    static int[] maxTree;
    static int S;
    static final int INF = Integer.MAX_VALUE;
    static int resultMin, resultMax;

    static void query(int a, int b) {
        int l = S + a - 1;
        int r = S + b - 1;
        int min = INF;
        int max = 0;
        
        while (l <= r) {
            if (l % 2 == 1) {
                min = Math.min(min, minTree[l]);
                max = Math.max(max, maxTree[l]); 
                l++; 
            }
            if (r % 2 == 0) {
                min = Math.min(min, minTree[r]);
                max = Math.max(max, maxTree[r]); 
                r--;
            }
            l /= 2;
            r /= 2;
        }
        resultMin = min;
        resultMax = max;
    }

    public static void main(String[] args) throws Exception {
    	System.setIn(new FileInputStream("res/class_B_low/input2357.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        S = 1;
        while (S < N) {
            S *= 2;
        }

        minTree = new int[S * 2];
        maxTree = new int[S * 2];
        
        Arrays.fill(minTree, INF);

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            minTree[S + i] = num;
            maxTree[S + i] = num;
        }

        for (int i = S - 1; i > 0; i--) {
            minTree[i] = Math.min(minTree[i * 2], minTree[i * 2 + 1]);
            maxTree[i] = Math.max(maxTree[i * 2], maxTree[i * 2 + 1]);
        }

        int a, b;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            
            query(a, b);
            
            sb.append(resultMin).append(' ').append(resultMax).append('\n');
        }
        System.out.println(sb);
    }
}