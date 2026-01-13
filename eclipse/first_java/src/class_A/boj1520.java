package class_A;

import java.io.*;
import java.util.*;

public class boj1520 {

	static int[][] dxy = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
	static int answer = 0;
	static int N, M;
	static int[][] memo;
	static int[][] arr;
	
	static int dfs(int x, int y) {
		if (x == N - 1 && y == M - 1) {
			return 1;
		}
		if (memo[x][y] != -1) {
			return memo[x][y];
		}
		
		memo[x][y] = 0;
		
		int num;
		num = arr[x][y];
		
		for (int[] d : dxy) {
			int nx = x + d[0];
			int ny = y + d[1];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M || arr[nx][ny] >= num) continue;
			memo[x][y] += dfs(nx, ny);
		}			
			
		return memo[x][y];
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input1520.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N][M];
		memo = new int[N][M];
//		memo -1로 초기화, arr 받기
		
		for (int i = 0; i < N; i++) {
			StringTokenizer line = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(line.nextToken());
				memo[i][j] = -1;
			}	
		}
		System.out.println(dfs(0,0));
	}

}

