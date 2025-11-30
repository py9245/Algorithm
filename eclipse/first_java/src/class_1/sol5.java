package class_1;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class sol5 {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input5.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		if ((N % 4 == 0 && N % 100 != 0) || N % 400 == 0) {
			System.out.println(1);
		} else {
			System.out.println(0);			
		}
	}

}
