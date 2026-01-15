package class_A;

import java.io.*;
import java.util.*;

public class boj1197 {
	
	static class Edge implements Comparable<Edge>{
		int to;
		long cost;
		
		public Edge(int to,  long cost) {
			this.to = to;
			this.cost = cost;
		}
		
		@Override
		public int compareTo(Edge o) {
			return (int)(this.cost - o.cost);
		}
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1197.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int v = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		ArrayList<Edge>[] node = new ArrayList[v + 1];
		
		for (int i = 0; i < v + 1; i++) {
			node[i] = new ArrayList<Edge>();
		}
		
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			node[a].add(new Edge(b, c));
			node[b].add(new Edge(a, c));
		}
		
		boolean[] visi = new boolean[v + 1];

		int cnt = v;
		
		pq.add(new Edge(1, 0));
		
		
		int answer = 0;
		while (!pq.isEmpty() && cnt > 0) {
			Edge c = pq.poll();
			if(visi[c.to]==true) continue;
			visi[c.to] = true;
			--cnt;
			answer += c.cost;

			for (Edge a : node[c.to]) {
				if (!visi[a.to]) {
					pq.add(a);
				}
			}
		}
		System.out.println(answer);
	}
}
