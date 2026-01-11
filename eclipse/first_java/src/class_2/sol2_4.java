package class_2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class sol2_4 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input4.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String N = br.readLine();
		int answer = 0;
		int end = Integer.parseInt(N);
		for (int i = end - N.length() * 9; i <= end - N.length(); i++) {
			String str = String.valueOf(i);
			int num = i;
			for (int j = 0; j < str.length(); j++) {
				num += str.charAt(j) - '0';
			}
			if (end == num) {
				answer = i;
				break;
			}
		}
		System.out.println(answer);

	}

}
