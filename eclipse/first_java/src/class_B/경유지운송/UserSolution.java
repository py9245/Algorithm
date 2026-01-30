package class_B.경유지운송;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.PriorityQueue;
import java.util.Set;

class UserSolution {
	
//	N 최대 1000 K최대 3400
	
	static int n, k;
	

	static class Edge implements Comparable<Edge>{
		int v, w;
		Edge(int v, int w){
			this.v = v;
			this.w = w;
		}
		public int compareTo(Edge o) {
			return o.w - this.w;
		}
	}
	
	static final int MAXL = 30001;
	static ArrayList<Edge>[] edge;
	static PriorityQueue<Edge> pq;
	static int[] dist;
	static boolean[] visi;
	static Set<Integer> need;
	static int remain;
	
	public void init(int N, int K, int sCity[], int eCity[], int mLimit[]) {
		n = N;
		k = K;
		edge = new ArrayList[n];
		
		for (int i = 0; i < n; i++) {
			edge[i] = new ArrayList<Edge>();
		}
		for (int i = 0; i < k; i++) {
			add(sCity[i], eCity[i], mLimit[i]);
		}
		return;
	}

	public void add(int sCity, int eCity, int mLimit) {
		edge[sCity].add(new Edge(eCity, mLimit));
		edge[eCity].add(new Edge(sCity, mLimit));
		return;
	}

	public int calculate(int sCity, int eCity, int M, int mStopover[]) {
	    pq = new PriorityQueue<>();
	    dist = new int[n];
	    visi = new boolean[n];

	    HashSet<Integer> needAll = new HashSet<>();
	    for (int i = 0; i < M; i++) {
	    	needAll.add(mStopover[i]);	    	
		} 
	    needAll.add(sCity);
	    needAll.add(eCity);

	    HashSet<Integer> remainSet = new HashSet<>(needAll);
	    remain = remainSet.size();

	    pq.add(new Edge(sCity, MAXL));
	    dist[sCity] = MAXL;

	    while (!pq.isEmpty() && remain > 0) {
	        Edge curr = pq.poll();

	        if (visi[curr.v]) continue;
	        visi[curr.v] = true;

	        if (remainSet.remove(curr.v)) remain--;

	        for (Edge next : edge[curr.v]) {
	            int nextW = Math.min(curr.w, next.w);
	            if (dist[next.v] >= nextW) continue;
	            dist[next.v] = nextW;
	            pq.add(new Edge(next.v, nextW));
	        }
	    }

	    if (remain != 0) return -1;

	    int answer = MAXL;
	    for (int x : needAll) {
	        answer = Math.min(answer, dist[x]);
	    }
	    return answer;
	}

}