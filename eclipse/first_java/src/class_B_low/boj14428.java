package class_B_low;

import java.io.*;
import java.util.*;

public class boj14428 {

	static int N, M, S;
	static final int INF = Integer.MAX_VALUE;
	static int[] nums, tree;

	static int getWinner(int x, int y) {
		if (x == 0)
			return y;
		if (y == 0)
			return x;
		if (nums[x] == nums[y])
			return Math.min(x, y);
		return (nums[x] < nums[y]) ? x : y;
	}

	static void update(int x, int y) {
		nums[x] = y;

		int curr = S + x - 1;
		curr /= 2;

		while (curr > 0) {
			tree[curr] = getWinner(tree[curr * 2], tree[curr * 2 + 1]);
			curr /= 2;
		}

	}

	static int query(int x, int y) {
		int minidx = x;
		int l = S + x - 1;
		int r = S + y - 1;

		while (l <= r) {
			if (l % 2 == 1)
				minidx = getWinner(minidx, tree[l++]);
			if (r % 2 == 0)
				minidx = getWinner(minidx, tree[r--]);
			l /= 2;
			r /= 2;
		}

		return minidx;
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/class_B_low/input14428.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		nums = new int[N + 1];
		for (int i = 1; i < N + 1; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		nums[0] = INF;

		S = 1;
		while (S < N) {
			S *= 2;
		}

		tree = new int[S * 2];

		for (int i = 0; i < N; i++) {
			tree[S + i] = i + 1;
		}

		for (int i = S - 1; i > 0; i--) {
			tree[i] = getWinner(tree[i * 2], tree[i * 2 + 1]);
		}

		M = Integer.parseInt(br.readLine());

		int cmd, a, b;
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			cmd = Integer.parseInt(st.nextToken());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			if (cmd == 1) {
				update(a, b);
			} else
				sb.append(query(a, b)).append("\n");
		}
		System.out.println(sb);
	}

}
