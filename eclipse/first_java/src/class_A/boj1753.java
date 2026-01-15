package class_A;

import java.io.*;
import java.util.*;

public class boj1753 {
	
	static final int INF = 1000000000;
	
	static class Edge implements Comparable<Edge>{
		int v, w;
		
		public Edge(int v, int w) {
			this.v = v;
			this.w = w;
		}
		
		public int compareTo(Edge o) {
			return this.w - o.w;
		}
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1753.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int v = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		
		int start = Integer.parseInt(br.readLine()) - 1;
		
		ArrayList<Edge>[] info = new ArrayList[v];
		int[] dist = new int[v];
		
		for (int i = 0; i < v; i++) {
			info[i] = new ArrayList<Edge>();
			dist[i] = INF;
		}
		
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken()) - 1;
			int to = Integer.parseInt(st.nextToken()) - 1;
			int cost = Integer.parseInt(st.nextToken());
			
			info[from].add(new Edge(to, cost));
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
		pq.add(new Edge(start, 0));
		dist[start] = 0;
		
		StringBuilder sb = new StringBuilder();
		
		while (!pq.isEmpty()) {
			Edge curr = pq.poll();
			
			if (curr.w > dist[curr.v]) continue;
			
			
			for (Edge edge : info[curr.v]) {
				int nextW = curr.w + edge.w;
				if (dist[edge.v] <= nextW) continue;
				dist[edge.v] = nextW;
				pq.add(new Edge(edge.v, nextW));
			}
			
		}
		for (int i = 0; i < dist.length; i++) {
			if (dist[i] == INF) sb.append("INF"+"\n");
			else sb.append(dist[i] + "\n");
		}
		System.out.println(sb);
	}

}

