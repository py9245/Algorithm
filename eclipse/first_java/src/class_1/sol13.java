package class_1;

import java.io.*;

public class sol13 {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input13.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			int score = 0;
			int current = 0;
			for (int j = 0; j < line.length(); j++) {
				if(line.charAt(j) == 'O') {
					current += 1;
					score += current;
				}
				else current = 0;
			}
			sb.append(score).append("\n");
		}
		System.out.println(sb);
	}
}
