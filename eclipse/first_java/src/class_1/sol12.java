package class_1;

import java.io.*;
import java.util.StringTokenizer;

public class sol12 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input12.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = 8;
		int[] nums = new int[8];
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		boolean a = true;
		boolean b = true;

		for (int i = 1; i < nums.length; i++) {
			if (nums[i] > nums[i - 1]) b = false;
			if (nums[i] < nums[i - 1]) a = false;
		}
		if (a) System.out.println("ascending");
		else if (b) System.out.println("descending");
		else System.out.println("mixed");
	}

}
