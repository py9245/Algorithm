//package class_A;
//
//import java.io.*;
//import java.util.*;
//
//public class boj1202 {
//
//	static class Jewel implements Comparable<Jewel> {
//		int weight;
//		int value;
//
//		public Jewel(int weight, int value) {
//			this.weight = weight;
//			this.value = value;
//		}
//
//		@Override
//		public int compareTo(Jewel o) {
//			return this.weight - o.weight;
//		}
//	}
//
//	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/class_A/input1202.txt"));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		int N = Integer.parseInt(st.nextToken());
//		int K = Integer.parseInt(st.nextToken());
//
//		Jewel[] jewels = new Jewel[N];
//
//		for (int i = 0; i < N; i++) {
//			st = new StringTokenizer(br.readLine());
//			int w = Integer.parseInt(st.nextToken());
//			int v = Integer.parseInt(st.nextToken());
//			jewels[i] = new Jewel(w, v);
//		}
//		int[] bags = new int[K];
//
//		for (int i = 0; i < K; i++) {
//			bags[i] = Integer.parseInt(br.readLine());
//		}
//
//		Arrays.sort(jewels);
//		Arrays.sort(bags);
//
//		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
//
//		long sum = 0;
//		int jIndex = 0;
//
//		for (int i = 0; i < K; i++) {
//			int currWeight = bags[i];
//
//			while (jIndex < N && jewels[jIndex].weight <= currWeight) {
//				pq.add(jewels[jIndex].value);
//				jIndex++;
//			}
//			if (!pq.isEmpty()) {
//				sum += pq.poll();
//			}
//		}
//		System.out.println(sum);
//	}
//}

package class_A;

import java.io.*;
import java.util.*;

public class boj1202 {

	static class Jewel implements Comparable<Jewel> {
		int weight;
		int value;

		public Jewel(int weight, int value) {
			this.weight = weight;
			this.value = value;
		}

		@Override
		public int compareTo(Jewel o) {
			return this.weight - o.weight;
		}
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_A/input1202.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		Jewel[] jewels = new Jewel[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			jewels[i] = new Jewel(w, v);
		}

		Arrays.sort(jewels);

		int[] bags = new int[K];

		for (int i = 0; i < K; i++) {
			bags[i] = Integer.parseInt(br.readLine());
		}

		Arrays.sort(bags);

		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

		int answer = 0;
		int jIndex = 0;

		for (int i = 0; i < K; i++) {
			int currweight = bags[i];

			while (jIndex < N && jewels[jIndex].weight <= currweight) {
				pq.add(jewels[jIndex].value);
				jIndex++;
			}
			if (!pq.isEmpty())answer += pq.poll();

		}
		System.out.println(answer);
	}

}