package class_1;

import java.io.*;
import java.util.*;

public class sol2 {

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input2.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		if (A > B) {
			System.out.println(">");
		} else if (B > A) {
			System.out.println("<");
		} else {
			System.out.println("==");
		}
	}
}
