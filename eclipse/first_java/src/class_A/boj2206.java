package class_A;

import java.io.*;
import java.util.*;

public class boj2206 {

	static int[][] dxy = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

	static class Node {
		int x, y, cnt;
		int used; // 0이면 안 부숨, 1이면 부숨

		// 생성자 (파이썬의 __init__ 같은 녀석)
		public Node(int x, int y, int cnt, int used) {
			this.x = x;
			this.y = y;
			this.cnt = cnt;
			this.used = used;
		}
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_A/input2206.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}

		int[][][] dist = new int[N][M][2];

		Deque<int[]> deque = new ArrayDeque<>();
		deque.addLast(new int[] { 0, 0, 1, 0 });
		dist[0][0][0] = 1;
		dist[0][0][1] = 1;
		boolean finished = false;

		while (!deque.isEmpty()) {
			int[] queue = deque.removeFirst();
			int x = queue[0];
			int y = queue[1];
			int cnt = queue[2];
			int used = queue[3];

			if (x == N - 1 && y == M - 1) {
				System.out.println(cnt);
				finished = true;
				break;
			}

			for (int[] d : dxy) {
				int nx = x + d[0];
				int ny = y + d[1];

				if (nx < 0 || nx >= N || ny < 0 || ny >= M)
					continue;

				if (arr[nx][ny] == 1) {

					if (used == 0 && dist[nx][ny][1] == 0) {
						dist[nx][ny][1] = cnt + 1;
						deque.addLast(new int[] { nx, ny, cnt + 1, 1 });
					}
				}

				else {
					if (dist[nx][ny][used] == 0) {
						dist[nx][ny][used] = cnt + 1;
						deque.addLast(new int[] { nx, ny, cnt + 1, used });
					}
				}
			}

		}
		if (!finished)
			System.out.println(-1);
	}

}
