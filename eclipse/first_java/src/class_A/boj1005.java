package class_A;

import java.io.*;
import java.util.*;

public class boj1005 {

    static int target;
    static int[] role;
    static ArrayList<Integer>[] parent;
    static long[] dp;

    static long dfs(int curr) {

        if (dp[curr] != -1) {
            return dp[curr];
        }
        
        long maxTime = 0;
        
        for (int i = 0; i < parent[curr].size(); i++) {
            int prevNode = parent[curr].get(i);
            
            maxTime = Math.max(maxTime, dfs(prevNode));
        }

        dp[curr] = maxTime + role[curr];
        
        return dp[curr];
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("res/class_A/input1005.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            role = new int[N];
            dp = new long[N];

            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                role[i] = Integer.parseInt(st.nextToken());
                dp[i] = -1;
            }

            parent = new ArrayList[N];

            for(int i = 0; i < N; i++) {
                parent[i] = new ArrayList<>();
            }

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int need = Integer.parseInt(st.nextToken()) - 1;
                int building = Integer.parseInt(st.nextToken()) - 1;
                
                parent[building].add(need);
            }

            target = Integer.parseInt(br.readLine()) - 1;

            System.out.println(dfs(target));
        }
    }
}