package class_A;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj1949 {

	static int N;
	static int[] people, depth;
	static int[][] dp;
	static ArrayList<Integer>[] node;
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/1949.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		people = new int[N + 1];
		depth = new int[N + 1];
		dp = new int[2][N + 1];

		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i < N + 1; i++) {
			people[i] = Integer.parseInt(st.nextToken());

		}
		
		node = new ArrayList[N + 1];
		
		for (int i = 0; i < N + 1; i++) {
			node[i] = new ArrayList<Integer>();
		}
		
		
		int a, b;
		
		for (int i = 0; i < N - 1; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			node[a].add(b);
			xxx[a] -= people[b];
			node[b].add(a);
			xxx[b] -= people[a];
		}
		System.out.println(Arrays.toString(xxx));
	}
}
