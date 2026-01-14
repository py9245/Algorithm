package class_A;

import java.io.*;
import java.util.*;

public class boj1916 {

	static final int INF = 1000000000;
	static int N, M;
	static long[] dist;

	static class Bus implements Comparable<Bus> {
		long cost;
		int target;

		public Bus(long cost, int target) {
			this.cost = cost;
			this.target = target;
		}
		
		public int compareTo(Bus o) {
			return (int) (this.cost - o.cost);
		}
	}

	static ArrayList<Bus>[] bus;
	static PriorityQueue<Bus> pq;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_A/input1916.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		bus = new ArrayList[N + 1];
		
		dist = new long[N + 1];
		
		for (int i = 0; i < N + 1; i++) {
			dist[i] = INF;
			bus[i] = new ArrayList<>();
		}
		
		StringTokenizer st;
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int target = Integer.parseInt(st.nextToken());
			long cost = Integer.parseInt(st.nextToken());
			bus[from].add(new Bus(cost, target));
		}
		
		st = new StringTokenizer(br.readLine());
		
		int startBus = Integer.parseInt(st.nextToken());
		int endBus = Integer.parseInt(st.nextToken());
		
		pq = new PriorityQueue<Bus>();
		pq.add(new Bus(0, startBus));
		dist[startBus] = 0;
		
		while (!pq.isEmpty()) {
			Bus c = pq.poll();
			
			int currBus = c.target;
			long currCost = c.cost;
			
			if (currBus == endBus) {
				System.out.println(currCost);
				return;
			}
			
			if(dist[currBus] < currCost) continue;
			
			
			
			for (Bus nxt : bus[currBus]) {
				int nxtBus = nxt.target;
				long nxtCost = nxt.cost + currCost;
				
				if (dist[nxtBus] <= nxtCost) continue;
				
				dist[nxtBus] = nxtCost;
				pq.add(new Bus(nxtCost, nxtBus));
			}
		}
		
	}

}
