package class_B_low;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj17435 {

	static final int LOG = 19;
	static int M, Q;
	static int[] nums;
	static int[][] logArr;
	
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_B_low/17435.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		M = Integer.parseInt(br.readLine());
		nums = new int[M + 1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i < M + 1; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		logArr = new int[LOG][M + 1];
		
		for (int i = 1; i < M + 1; i++) {
			logArr[0][i] = nums[i];
		}
		
		for (int k = 1; k < LOG; k++) {
			for (int i = 1; i < M + 1; i++) {
				logArr[k][i] = logArr[k - 1][logArr[k - 1][i]];
			}
		}
		
		
		StringBuilder sb = new StringBuilder();
		Q = Integer.parseInt(br.readLine());
		
		int n, x;
		
		for (int q = 0; q < Q; q++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			x = Integer.parseInt(st.nextToken());
			
			for (int k = 0; k < LOG; k++) {
				if ((n & (1 << k)) != 0) {
					x = logArr[k][x];
				}
			}
			sb.append(x).append("\n");
		}
		System.out.println(sb);
	}

}
