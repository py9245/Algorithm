package class_A;

import java.io.*;
import java.util.*;

public class boj1197 {
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1197.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int v = Integer.parseInt(st.nextToken());
		int e = Integer.parseInt(st.nextToken());
		
		
		PriorityQueue<int[]> edge = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
		
		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
		}
	}
}
