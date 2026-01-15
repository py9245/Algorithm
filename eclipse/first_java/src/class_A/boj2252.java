package class_A;

import java.io.*;
import java.util.*;

public class boj2252 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_A/input2252.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		
		ArrayList<Integer>[] graph = new ArrayList[n + 1];
		int[] indegree = new int[n + 1]; // "내 앞에 몇 명?"
		
		for (int i = 1; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()); // a가
			int b = Integer.parseInt(st.nextToken()); // b 앞에 선다 (a -> b)
			
		
			graph[a].add(b);
			indegree[b]++;
		}
		
		
		Queue<Integer> q = new ArrayDeque<>();
		
		for (int i = 1; i <= n; i++) {
		
			 if (indegree[i] == 0) {
			     q.add(i);
			 }
		}
		
		StringBuilder sb = new StringBuilder();
		
		
		while (!q.isEmpty()) {
			int curr = q.poll();
			sb.append(curr).append(" ");
			
			
			for (int next : graph[curr]) {
				indegree[next]--;
				
				if (indegree[next] == 0) {
				    q.add(next);
				}
			}
		}
		
		System.out.println(sb);
	}
}