package class_B.전기차여행;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

class UserSolution {
	
	static int n, m, k;
	
	static class Edge implements Comparable<Edge>{
		int eID, to, time, power;
		
		public Edge(int to, int time, int power) {
			this.to = to;
			this.time = time;
			this.power = power;
		}
		public int compareTo(Edge o) {
			return this.time - o.time;
		}
	}
	
	static class NodeV implements Comparable<NodeV>{
		int arrived, city;
		
		public NodeV(int arrived, int city) {
			this.arrived = arrived;
			this.city = city;
		}
		
		public int compareTo(NodeV o) {
			return this.arrived - o.arrived;
		}
	}
	
	static class NodeC implements Comparable<NodeC>{
		int arrived, city, power;
		
		public NodeC(int arrived, int city, int power) {
			this.arrived = arrived;
			this.city = city;
			this.power = power;
		}
		
		public int compareTo(NodeC o) {
			return this.arrived - o.arrived;
		}
	}
	
	static int[] charge;
//	key = 도로 ID val = 출발 위치 remove를 위한
	static HashMap<Integer, Integer> edgeinfo;
	static ArrayList<Edge>[] edge;
	static PriorityQueue<NodeV> vPQ;
	static PriorityQueue<NodeC> cPQ;
//	도시는 0 ~ N - 1 ID 도시엔 충전소 단위 시간당 충전량
//	도로는 단방향 도로 ID, 소요시간, 전력소모량
//	M개의 도시에서 전염병 발생(발생 시기 상이할 수 있음)
//	전염병 부터 다익스트라 돌고
	
	
	public void init(int N, int mCharge[], int K, int mId[], int sCity[], int eCity[], int mTime[], int mPower[]) {
		n = N;
		k = K;
		charge = new int[n];
		edgeinfo = new HashMap<Integer, Integer>();
		edge = new ArrayList[n];
		for (int i = 0; i < n; i++) {
			edge[i] = new ArrayList<Edge>();
		}
		for (int i = 0; i < n; i++) {
			charge[i] = mCharge[i];
		}
		for (int i = 0; i < k; i++) {
			int mid = mId[i];
			int scity = sCity[i];
			edgeinfo.put(mid, scity);
			Edge curr = new Edge(eCity[i], mTime[i], mPower[i]);
			curr.eID = mid;
			edge[scity].add(curr);
		}
		
		
		return;
	}

	public void add(int mId, int sCity, int eCity, int mTime, int mPower) {
		edgeinfo.put(mId, sCity);
		Edge curr = new Edge(eCity, mTime, mPower);
		curr.eID = mId;
		edge[sCity].add(curr);
		return;
	}

	public void remove(int mId) {
		Integer startObj = edgeinfo.remove(mId);
		if (startObj == null )return;
		int start = startObj;
		for (int i = 0; i < edge[start].size(); i++) {
			if (edge[start].get(i).eID == mId) {
				edge[start].remove(i);
				return;
			}
		}
		return;
	}
	
	static int[] dist, danger;
	static final int INF = Integer.MAX_VALUE;
	
	public int cost(int B, int sCity, int eCity, int M, int mCity[], int mTime[]) {
		m = M;
		int answer = -1;
		danger = new int[n];
		dist = new int[n];
		for (int i = 0; i < n; i++) {
			danger[i] = INF;
			dist[i] = INF;
		}
		vPQ = new PriorityQueue<NodeV>();
		
		for (int i = 0; i < M; i++) {
			vPQ.add(new NodeV(mTime[i], mCity[i]));
			danger[mCity[i]] = mTime[i];
		}
		
		while (!vPQ.isEmpty()) {
			NodeV curr = vPQ.poll();
			
			if (curr.arrived > danger[curr.city]) continue;
			for (Edge next : edge[curr.city]) {
				int nextarrived = curr.arrived + next.time;
				if (danger[next.to] <= nextarrived) continue;
				danger[next.to] = nextarrived;
				vPQ.add(new NodeV(nextarrived, next.to));
			}
		}
		
		cPQ = new PriorityQueue<NodeC>();
		cPQ.add(new NodeC(0, sCity, B));
		dist[sCity] = 0;
		while (!cPQ.isEmpty()) {
			NodeC curr = cPQ.poll();
			if (dist[curr.city] < curr.arrived || danger[curr.city] <= curr.arrived)continue;
			if (curr.city ==  eCity)
				return curr.arrived;
			for (Edge next : edge[curr.city]) {
				int currP = curr.power;
				int nextarrived = curr.arrived + next.time;
				while (currP < next.power) {
					nextarrived++;
					currP += charge[curr.city];
				}
				currP -= next.power;
				if (nextarrived >= dist[next.to] || nextarrived >= danger[next.to]) continue;
				cPQ.add(new NodeC(nextarrived, next.to, currP));
				dist[next.to] = nextarrived;
			}
			
		}
		
		return answer;
	}
}