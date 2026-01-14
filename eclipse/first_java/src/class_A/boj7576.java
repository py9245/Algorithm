package class_A;

import java.io.*;
import java.util.*;

public class boj7576 {
	
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	
	static class Tomato{
		int x, y;
		
		public Tomato(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input7576.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[][] tomatos = new int[N][M];
		int counter = N * M;
		
		Deque<Tomato> q = new ArrayDeque<>();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				int status = Integer.parseInt(st.nextToken());
				tomatos[i][j] = status;
				if (status == 1) {
					counter--;
					q.add(new Tomato(i, j));
				}else if (status == -1) --counter;
				
			}
		}
		int answer = 0;

		
		while (!q.isEmpty() && counter > 0) {
			int qsize = q.size();
			answer++;
			while (qsize > 0 && !q.isEmpty() && counter > 0) {
				qsize--;
				
				Tomato c = q.poll();
				
				for (int i = 0; i < 4; i++) {
					int nx = c.x + dx[i];
					int ny = c.y + dy[i];
					
					if(nx < 0 || ny < 0 || nx >= N || ny >= M || tomatos[nx][ny] != 0) continue;
					counter--;
					tomatos[nx][ny] = 1;
					q.add(new Tomato(nx, ny));
					
				}

			}
			
		}
		if (counter > 0) answer = -1;
		System.out.println(answer);
	}

}
