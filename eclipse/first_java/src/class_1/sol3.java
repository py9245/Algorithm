package class_1;

import java.io.*;

public class sol3 {

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input3.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		String str = "*";
		
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j < i; j++) {
				sb.append(str);
			}
			sb.append("\n");
		}
		
		System.out.print(sb);
	}

}