package class_A;

import java.io.*;
import java.util.*;

public class boj1005_ver2 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1005.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int n, k;
		int[] cost, result, degree;
		List<Integer>[] building;
		Deque<Integer> q;
		
		for (int tc = 0; tc < t; tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			cost = new int[n];
			result = new int[n];
			degree = new int[n];
			building = new ArrayList[n];
			
			
			st = new StringTokenizer(br.readLine());
			
			for (int i = 0; i < n; i++) {
				cost[i] = Integer.parseInt(st.nextToken());
				building[i] = new ArrayList<Integer>();
			}
			
			for (int i = 0; i < k; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken()) - 1;
				int b = Integer.parseInt(st.nextToken()) - 1;
				building[a].add(b);
				degree[b]++;
			}
						
			int target = Integer.parseInt(br.readLine()) - 1;
			
			q = new ArrayDeque<Integer>();

			for (int i = 0; i < n; i++) {
				if (degree[i] == 0) q.add(i);
				result[i] = cost[i];
			}

			while (!q.isEmpty()) {
				int curr = q.poll();
				
				for (Integer next : building[curr]) {
					result[next] = Math.max(result[next], result[curr] + cost[next]);
					degree[next]--;
					if (degree[next] == 0) q.add(next);
				}
			}
			System.out.println(result[target]);
		}
	}

}
