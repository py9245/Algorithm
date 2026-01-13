package class_A;

import java.io.*;
import java.util.*;

public class swea1961 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1961.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[][][] arr = new int[N][N][4];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j][0] = Integer.parseInt(st.nextToken());
				}
			}
			
			
			sb.append("#" + tc + "\n");

			int idx = N - 1;
			for (int r = 1; r < 4; r++) {				
				for (int j = 0; j < N; j++) {
					for (int i = idx; i >= 0; i--) {
						arr[j][idx - i][r] = arr[i][j][r - 1];
					}
				}
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = 1; j < 4; j++) {
					for (int j2 = 0; j2 < N; j2++) {
						sb.append(arr[i][j2][j]);
					}
					sb.append(" ");
				}
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}

}
