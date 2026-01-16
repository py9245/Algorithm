package class_A;

import java.io.*;
import java.util.*;

public class boj1647 {
	
	static BufferedReader br;
	static StringTokenizer st;
	static int n, m;
	static int[] parent;
	
	static class Edge implements Comparable<Edge>{
		int x, y, cost;
		
		public Edge(int x, int y, int cost) {
			this.x = x;
			this.y = y;
			this.cost = cost;
		}
		
		public int compareTo(Edge o) {
			return this.cost - o.cost;
		}
	} 
	
	static PriorityQueue<Edge> pq;
	
	static int find(int x) {
		if (parent[x] != x) parent[x] = find(parent[x]);
		return parent[x];
	}
	
	static boolean union(int x, int y) {
		int rootX = find(x);
		int rootY = find(y);
		if (rootX != rootY) {
			parent[rootY] = rootX;
			return true;
		}
		return false;
	}
	
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1647.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		if (n == 2) {
			System.out.println(0);
			return;
		}
		
		parent = new int[n + 1];
		
		for (int i = 0; i < n + 1; i++) {
			parent[i] = i;
		}
		
		pq = new PriorityQueue<Edge>();
		
		int a, b, c;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			pq.add(new Edge(a, b, c));
		}
		
		int totalCost = 0;
		int edgeCount = 0;
		
		
		while (!pq.isEmpty()) {
			Edge curr = pq.poll();
			if (union(curr.x, curr.y)) {
				totalCost += curr.cost;
				edgeCount ++;
				if (edgeCount == n - 2) {					
					System.out.println(totalCost);
					return;
				}
			}
		}
	}

}
