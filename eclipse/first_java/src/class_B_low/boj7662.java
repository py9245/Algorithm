package class_B_low;

import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class boj7662 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_B_low/7662.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		TreeMap<Integer, Integer> map;
		StringTokenizer st;
		for (int i = 0; i < T; i++) {
			int K = Integer.parseInt(br.readLine());
			map = new TreeMap<Integer, Integer>();
			for (int j = 0; j < K; j++) {
				st = new StringTokenizer(br.readLine());
				String cmd = st.nextToken();
				int num = Integer.parseInt(st.nextToken());
				int cnt = map.getOrDefault(num, 0);
				if (cmd.equals("I")) {
					map.put(num, cnt + 1);
				} else if (!map.isEmpty()){
					if (num == 1) {
						Entry<Integer, Integer> curr = map.pollLastEntry();
						map.put(curr.getKey(), Math.max(0, curr.getValue() - 1));
						if (map.get(curr.getKey())==0)map.remove(curr.getKey());
					} else {
						Entry<Integer, Integer> curr = map.pollFirstEntry();
						map.put(curr.getKey(), Math.max(0, curr.getValue() - 1));
						if (map.get(curr.getKey())==0)map.remove(curr.getKey());
					}
					
				}
			}
			StringBuilder tc = new StringBuilder();
			if (map.isEmpty())tc.append("EMPTY");
			else tc.append(map.lastKey()).append(" ").append(map.firstKey());
			sb.append(tc).append("\n");
		}
		System.out.println(sb);
	}

}
