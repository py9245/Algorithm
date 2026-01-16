package class_A;

import java.io.*;
import java.util.*;

public class boj1766 {

	static int n, m;
	static List<Integer>[] nums;
	static int[] degree;
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1766.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		nums = new ArrayList[n + 1];
		degree = new int[n + 1];
		for (int i = 0; i < n + 1; i++) {
			nums[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			nums[a].add(b);
			degree[b]++;
		}
		
		PriorityQueue<Integer> q = new PriorityQueue<Integer>();
		
		for (int i = 1; i < n + 1; i++) {
			if (degree[i] == 0) q.add(i);
		}
		
		StringBuilder sb = new StringBuilder();
		
		while (!q.isEmpty()) {
			int curr = q.poll();
			sb.append(curr).append(" ");
			
			
			for (int next : nums[curr]) {
				degree[next]--;
				
				if (degree[next] == 0) {
				    q.add(next);
				}
			}
		}
		System.out.println(sb);
	}
}
