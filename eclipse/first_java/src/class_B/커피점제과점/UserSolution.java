package class_B.커피점제과점;

import java.util.*;

class UserSolution {
//	정점, 노드 받음
	static int n, k;
	
//	dist를 위한 최댓값 설정
	static final int INF = Integer.MAX_VALUE/2;
	
//	edge객체
	static class Edge implements Comparable<Edge>{
		int node, cost;
		
		public Edge(int node, int cost) {
			this.node = node;
			this.cost = cost;
		}
		@Override
		public int compareTo(Edge o) {
			return this.cost - o.cost;
		}
		
	}
	
	static ArrayList<Edge>[] building;
	static int m, p, r;
	static int[] cafeDist, bakeDist;
	static PriorityQueue<Edge> cafepq, bakepq;
	
	public void init(int N, int K, int sBuilding[], int eBuilding[], int mDistance[]) {
		n = N;
		k = K;
		building = new ArrayList[N + 1];
		for (int i = 0; i < N + 1; i++) {
			building[i] = new ArrayList<Edge>();
		}
		int s, e, c;
		for (int i = 0; i < K; i++) {
			s = sBuilding[i];
			e = eBuilding[i];
			c = mDistance[i];
			building[s].add(new Edge(e, c));
			building[e].add(new Edge(s, c));
		}
		return;
	}

	
	public void add(int sBuilding, int eBuilding, int mDistance) {
		k++;
		building[sBuilding].add(new Edge(eBuilding, mDistance));
		building[eBuilding].add(new Edge(sBuilding, mDistance));
		return;
	}

	public int calculate(int M, int mCoffee[], int P, int mBakery[], int R) {
		m = M;
		p = P;
		r = R;
		cafepq = new PriorityQueue<Edge>();
		bakepq = new PriorityQueue<Edge>();
		cafeDist = new int[n + 1]; 
		bakeDist = new int[n + 1];
		Arrays.fill(cafeDist, INF);
		Arrays.fill(bakeDist, INF);
		
		int mc;
		int mb;
		boolean[] visi = new boolean[n + 1];
		
		for (int i = 0; i < M; i++) {
			mc = mCoffee[i];
			visi[mc] = true;
			cafeDist[mc] = 0;
			cafepq.add(new Edge(mc, 0));
		}
		
		for (int i = 0; i < P; i++) {
			mb = mBakery[i];
			visi[mb] = true;
			bakeDist[mb] = 0;
			bakepq.add(new Edge(mb, 0));
		}
		
		
		while (!cafepq.isEmpty()) {
			Edge curr = cafepq.poll();
			
			if (cafeDist[curr.node] < curr.cost) continue;
			
			int nextCost;
			for (Edge next : building[curr.node]) {
				nextCost = curr.cost + next.cost;
				if (nextCost >= cafeDist[next.node] || nextCost > r) continue;
				cafeDist[next.node] = nextCost;
				cafepq.add(new Edge(next.node, nextCost));
			}
			
		}
		
		
		while (!bakepq.isEmpty()) {
			Edge curr = bakepq.poll();
			
			if (bakeDist[curr.node] < curr.cost) continue;
			
			int nextCost;
			for (Edge next : building[curr.node]) {
				nextCost = curr.cost + next.cost;
				if (nextCost >= bakeDist[next.node] || nextCost > r) continue;
				bakeDist[next.node] = nextCost;
				bakepq.add(new Edge(next.node, nextCost));
			}
			
		}
		int answer = INF;
		for (int i = 0; i < n + 1; i++) {
			if (visi[i]) continue;
			answer = Math.min(answer, cafeDist[i] + bakeDist[i]);
		}
		if (answer == INF) answer = -1;
		return answer;
	}
}