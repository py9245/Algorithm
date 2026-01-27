package class_B.전기차충전소;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

class UserSolution {
	
	static final int INF = Integer.MAX_VALUE;
	static int n, k;
	
//	정점 cost기록
	static int[] cost;
	
//	간선이 들어있는 정점 기록 remove용
	static HashMap<Integer, Integer> edgeinfo;
	
//	간선 클레스
	static class Edge{
		int uID, to, dist;
		
		public Edge(int uID, int to, int dist) {
			this.uID = uID;
			this.to = to;
			this.dist = dist;
		}
	}
//	간선들 저장
	static ArrayList<Edge>[] edge;
	
//	다익스트라용 node class
	static class Node implements Comparable<Node>{
		int node, dist, minNode;
		public Node(int node, int dist, int minNode) {
			this.node = node;
			this.dist = dist;
			this.minNode = minNode;
		}
		public int compareTo(Node o) {
			return this.dist - o.dist;
		}
	}
	
//	다익스트라용 pq
	static PriorityQueue<Node> pq;
	
//	dist 기록을 [도착정점][계산기준 코스트 정점]
	static int[][] dist;
	
	public void init(int N, int mCost[], int K, int mId[], int sCity[], int eCity[], int mDistance[]) {
		n = N;
		k = K;
		cost = new int[N];
		edgeinfo = new HashMap<Integer, Integer>();
		edge = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			cost[i] = mCost[i];
			edge[i] = new ArrayList<Edge>();
		}
		
		for (int i = 0; i < K; i++) {
			add(mId[i], sCity[i], eCity[i], mDistance[i]);
		}
		return;
	}

	public void add(int mId, int sCity, int eCity, int mDistance) {
		edgeinfo.put(mId, sCity);
		edge[sCity].add(new Edge(mId, eCity, mDistance));
		return;
	}

	public void remove(int mId) {
		int idx = edgeinfo.get(mId);
		for (int i = 0; i < edge[idx].size(); i++) {
			if (edge[idx].get(i).uID == mId) {
				edge[idx].remove(i);
				return;
			}
		}
		return;
	}

	public int cost(int sCity, int eCity) {
		pq = new PriorityQueue<Node>();
		dist = new int[n][n];
		for (int i = 0; i < n; i++) {			
			Arrays.fill(dist[i], INF);
		}
		pq.add(new Node(sCity, 0, sCity));
		dist[sCity][sCity] = 0;
		
		while (!pq.isEmpty()) {
			Node curr = pq.poll();
//			System.out.println("curr.node : " + curr.node + "  curr.dist : " + curr.dist + "  curr.min : " + curr.minNode);
			if (dist[curr.node][curr.minNode] < curr.dist) continue;
			
			if (curr.node == eCity) return curr.dist;
			
			for (Edge next : edge[curr.node]) {
				int nextDist = curr.dist + (cost[curr.minNode] * next.dist);
				int nextMinNode = (cost[curr.minNode] <= cost[next.to])? curr.minNode : next.to;
//				System.out.println(nextMinNode);
				if(dist[next.to][nextMinNode] <= nextDist) continue;
				dist[next.to][nextMinNode] = nextDist;
				pq.add(new Node(next.to, nextDist, nextMinNode));
			}
		}
		return -1;
	}
}