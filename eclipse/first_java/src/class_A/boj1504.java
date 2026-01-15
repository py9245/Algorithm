package class_A;

import java.io.*;
import java.util.*;

public class boj1504 {

	static final int INF = Integer.MAX_VALUE;
	static int v, e, a, b;
	static int[] dist;
	static PriorityQueue<Edge> pq;

	static class Edge implements Comparable<Edge> {
		int to, weight;

		public Edge(int to, int weight) {
			this.to = to;
			this.weight = weight;
		}

		public int compareTo(Edge o) {
			return this.weight - o.weight;
		}
	}

	static List<Edge>[] node;

	static int dijkstra(int s, int e) {
		Arrays.fill(dist, INF);
		dist[s] = 0;
		pq = new PriorityQueue<Edge>();
		pq.add(new Edge(s, 0));

		while (!pq.isEmpty()) {
			Edge curr = pq.poll();

			if (curr.weight > dist[curr.to])
				continue;

			if (curr.to == e) {
				return dist[curr.to];
			}

			for (Edge edge : node[curr.to]) {
				int nextWeight = curr.weight + edge.weight;
				if (dist[edge.to] <= nextWeight)
					continue;
				dist[edge.to] = nextWeight;
				pq.add(new Edge(edge.to, nextWeight));
			}
		}
		return -1;
	}

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1504.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		dist = new int[v];
		node = new ArrayList[v];
		for (int i = 0; i < v; i++) {
			node[i] = new ArrayList<Edge>();
		}
		
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()) - 1;
			int b = Integer.parseInt(st.nextToken()) - 1;
			int cost = Integer.parseInt(st.nextToken());
			node[a].add(new Edge(b, cost));
			node[b].add(new Edge(a, cost));
		}
		
		st = new StringTokenizer(br.readLine());
		
		a = Integer.parseInt(st.nextToken()) - 1;
		b = Integer.parseInt(st.nextToken()) - 1;
		
		
		int sToA = dijkstra(0, a);
		int sToB = dijkstra(0, b);
		int aToB = dijkstra(a, b);
		int aToE = dijkstra(a, v - 1);
		int bToE = dijkstra(b, v - 1);
		long res1 = -1;
	    if (sToA != -1 && aToB != -1 && bToE != -1) {
	        res1 = (long)sToA + aToB + bToE;
	    }

	    long res2 = -1;
	    if (sToB != -1 && aToB != -1 && aToE != -1) {
	        res2 = (long)sToB + aToB + aToE;
	    }

	    if (res1 == -1 && res2 == -1) {
	        System.out.println(-1);
	    } else if (res1 == -1) {
	        System.out.println(res2);
	    } else if (res2 == -1) {
	        System.out.println(res1);
	    } else {
	        System.out.println(Math.min(res1, res2));
	    }
	}
}
