package class_A;

import java.io.*;
import java.util.*;

public class boj21939 {

	static int N, M;
	static int[] trash = new int[100001];
	static StringBuilder sb = new StringBuilder();
	static class Problem{
		int pId, grade;
		
		public Problem(int pId, int grade) {
			this.pId = pId;
			this.grade = grade;
		}
	}
	
	static PriorityQueue<Problem> topDownPq, lowUpPq;
	
	static Comparator<Problem> lowUp = (o1, o2) -> {
		if (o1.grade != o2.grade) return o1.grade - o2.grade;
		return o1.pId - o2.pId;
	};
	
	static Comparator<Problem> topDown = (o1, o2) -> {
		if (o1.grade != o2.grade) return o2.grade - o1.grade;
		return o2.pId - o1.pId;
	};
	
	static void Add(int pId, int grade) {
		Problem curr = new Problem(pId, grade);
		topDownPq.add(curr);
		lowUpPq.add(curr);
		trash[pId] = grade;
	}
	
	static void Solved(int pId) {
		trash[pId] = 0;
	}
	
	static void Recommend(int type) {
		int answer = 0;
		if (type == 1) {
			while (answer == 0) {
				Problem curr = topDownPq.poll();
				if (trash[curr.pId] == 0 || trash[curr.pId] != curr.grade) continue;
				answer = curr.pId;
				topDownPq.add(curr);
			}
		} else {
			while (answer == 0) {
				Problem curr = lowUpPq.poll();
				if (trash[curr.pId] == 0 || trash[curr.pId] != curr.grade) continue;
				answer = curr.pId;
				lowUpPq.add(curr);
			}
		}
		sb.append(answer).append("\n");
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/21939.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		topDownPq = new PriorityQueue<Problem>(topDown);
		lowUpPq = new PriorityQueue<Problem>(lowUp);
		
		int a, b;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			Add(a, b);
			
		}
		
		M = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			a = Integer.parseInt(st.nextToken());
			if (cmd.equals("add")) {
				b = Integer.parseInt(st.nextToken());
				Add(a, b);
			}else if (cmd.equals("recommend")) {
				Recommend(a);
			}else {
				Solved(a);
			}
		}
		System.out.println(sb);
	}

}
