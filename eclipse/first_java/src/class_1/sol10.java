package class_1;

import java.io.*;
import java.util.*;

public class sol10 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input10.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int H = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			int idx = Integer.parseInt(st.nextToken()) - 1;
			System.out.println((idx % H + 1) * 100 + 1 + (int) idx / H);
		}
	}

}
