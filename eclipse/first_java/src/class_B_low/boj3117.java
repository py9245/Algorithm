package class_B_low;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj3117 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_B_low/3117.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int log = 1;
		int temp = 1;
		while (temp <= M) {
			temp *= 2;
			++log;
		}
		
		int[] query = new int[N];
		int[][] video = new int[log][K + 1];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			query[i] = Integer.parseInt(st.nextToken());
		}
				
		st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i < K + 1; i++) {
			video[0][i] = Integer.parseInt(st.nextToken());
			
		}
		
		for (int l = 1; l < log; l++) {
			for (int i = 1; i < K + 1; i++) {
				video[l][i] = video[l - 1][video[l - 1][i]];
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < N; i++) {
			int currIdx = query[i];
			for (int j = 0; j < log; j++) {
				if ((M - 1 & (1 << j)) != 0) {
					currIdx = video[j][currIdx];
				}
			}
			sb.append(currIdx).append(" ");
		}
		System.out.println(sb);
	}

}
