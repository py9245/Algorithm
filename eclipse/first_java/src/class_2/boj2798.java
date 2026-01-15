package class_2;

import java.io.*;
import java.util.*;

public class boj2798 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/class_2/input2798.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] nums = new int[n];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(nums);
		
		int best = 0;
		
		for (int i = 0; i < n - 2; i++) {
			int num1 = nums[i];
			if (num1 > m)break;
			for (int j = i + 1; j < n - 1; j++) {
				int num2 = num1 + nums[j];
				if (num2 > m)break;
				for (int j2 = j + 1; j2 < n; j2++) {
					int num = nums[i] + nums[j] + nums[j2];
					if (num2 > m)break;
					best = (num > best && num <= m) ? num : best;
				}
			}
		}
		System.out.println(best);
	}

}
