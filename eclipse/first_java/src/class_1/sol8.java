package class_1;

import java.io.*;

public class sol8 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input8.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(i);
			sb.append("\n");
		}
		System.out.println(sb);
	}

}
