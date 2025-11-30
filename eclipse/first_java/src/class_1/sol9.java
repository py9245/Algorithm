package class_1;

import java.io.*;

public class sol9 {

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/input9.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String A = br.readLine();
		String B = br.readLine();
		String C = br.readLine();

		int a = Integer.parseInt(A);
		int b = Integer.parseInt(B);
		int c = Integer.parseInt(C);

		int intAnswer = a + b - c;
		int stringAnswer = Integer.parseInt(A + B) - c;

		System.out.println(intAnswer);
		System.out.println(stringAnswer);

	}

}
