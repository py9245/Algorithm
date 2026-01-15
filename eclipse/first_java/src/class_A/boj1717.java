package class_A;

import java.io.*;
import java.util.StringTokenizer;

public class boj1717 {
	
	static int n, m;
	static int[] parent;
	
	static int find(int x) {
		if (parent[x] != x) parent[x] = find(parent[x]);
		return parent[x];
	}
	
	static void union(int x, int y) {
		int rootX = find(x);
		int rootY = find(y);
		if (rootX < rootY) parent[rootY] = rootX;
		else parent[rootX] = rootY;
	}
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_A/input1717.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		parent = new int[n + 1];
		for (int i = 0; i < n + 1; i++) {
			parent[i] = i;
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int cmd = Integer.parseInt(st.nextToken());
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken()); 
			if (cmd == 0) {
				union(num1, num2);
			} else {
				if (find(num1) == find(num2)) sb.append("YES" + "\n");
				else sb.append("NO" + "\n");
			}
		}
		System.out.println(sb);
	}
}
