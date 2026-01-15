package class_A;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class boj4195 {

	static int t, f, lastNum;
	static int[] size = new int[200005];
	static int[] parent = new int[200005];	
	static StringTokenizer st;
	static Map<String, Integer> friends;
	
	static int find(int x) {
		if (parent[x] != x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}
	
	static int union(int x, int y) {
		int rootX = find(x);
		int rootY = find(y);
		
		if (rootX != rootY) {
			parent[rootY] = rootX;
			size[rootX] += size[rootY]; 
		}
		
		return size[rootX];
	}
	
	public static void main(String[] args) throws Exception  {
		System.setIn(new FileInputStream("res/class_A/input4195.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		for (int tc = 1; tc <= t; tc++) {
			f = Integer.parseInt(br.readLine());
			
			for (int i = 0; i < f * 2; i++) {
				size[i] = 1;
				parent[i] = i;
			}
			
			lastNum = 0;
			friends = new HashMap<>();
			
			
			for (int i = 0; i < f; i++) {
				st = new StringTokenizer(br.readLine());
				
				String one = st.nextToken();
				String two = st.nextToken();
				
				int oneIdx = friends.getOrDefault(one, -1);
				int twoIdx = friends.getOrDefault(two, -1);
				
				if (oneIdx == -1) {
					oneIdx = lastNum;
					friends.put(one, lastNum++);
					
				}
				if (twoIdx == -1) {
					twoIdx = lastNum;
					friends.put(two, lastNum++);
				}
				sb.append(union(oneIdx, twoIdx));
				sb.append("\n");
				
			}
		}
		System.out.print(sb);
	}

}
