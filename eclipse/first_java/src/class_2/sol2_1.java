package class_2;

import java.io.*;
import java.util.StringTokenizer;

public class sol2_1 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			if (A == 0 && B == 0 && C == 0) break;
			int temp = A;
			if (A < B) {
				A = B;
				B = temp;
				temp = A;
			}
			if (A < C) {
				A = C;
				C = temp;
			}
			long answer = A * A - B * B - C * C;
			if (answer == 0) sb.append("right").append("\n");
			else sb.append("wrong").append("\n");
		}
		System.out.println(sb);
	}

}
