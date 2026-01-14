package class_A;

import java.io.*;
import java.util.*;

public class boj4179 {

	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_A/input4179.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		char[][] grid = new char[r][c];
		int startX = 0;
		int startY = 0;
		
		ArrayDeque<Node> fDeque = new ArrayDeque<>();
		ArrayDeque<Node> jDeque = new ArrayDeque<>();

		//		맨처음 맵을 받고 지훈이도 '.' 으로 일단 바꿈

		for (int i = 0; i < r; i++) {
			String line = br.readLine();
			for (int j = 0; j < c; j++) {
				char ch = line.charAt(j);
				if (ch == 'J') {
					jDeque.addLast(new Node(i, j));
					ch = '.';
				} else if (ch == 'F') {
					fDeque.addLast(new Node(i, j));
				}
				grid[i][j] = ch;
			}
		}
		
		int answer = 0;
		
		while (!jDeque.isEmpty()) {
			answer++;
			int fSize = fDeque.size();
			while (fSize-- > 0) {
				Node f = fDeque.poll();
				
				for (int i = 0; i < 4; i++) {
					int nx = f.x + dx[i];
					int ny = f.y + dy[i];
					
					if (nx < 0 || nx >= r || ny < 0 || ny >= c || grid[nx][ny] == 'F' || grid[nx][ny] == '#') continue;
					grid[nx][ny] = 'F';
					fDeque.add(new Node(nx, ny));
				}
			}
			int jSize = jDeque.size();
			
			while (jSize-- > 0) {
				Node j = jDeque.poll();
				
				for (int i = 0; i < 4; i++) {
					int nx = j.x + dx[i];
					int ny = j.y + dy[i];
					
					if (nx < 0 || nx >= r || ny < 0 || ny >= c) {
						System.out.println(answer);
						return;
					}
					if (grid[nx][ny] == '.') {
					grid[nx][ny] = 'J';
					jDeque.add(new Node(nx, ny));
					}
				}
			}
		}
		System.out.println("IMPOSSIBLE");
	}

}
