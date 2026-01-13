package class_1;

import java.io.*;

public class sol11 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input11.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int A = Integer.parseInt(br.readLine());
		int B = Integer.parseInt(br.readLine());
		int C = Integer.parseInt(br.readLine());
		String num = String.valueOf(A * B * C);
		int N = 10;
		int[] answer = new int[10];
		for (int i = 0; i < num.length(); i++) {
			answer[num.charAt(i) - '0'] += 1;
		}
		StringBuilder sb = new StringBuilder();
		for (int j = 0; j < N; j++) {
			sb.append(j);
			sb.append("\n");
		}
		System.out.println(sb);
	}

}
