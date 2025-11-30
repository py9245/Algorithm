package class_1;

import java.io.*;

public class sol4 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input4.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int score = Integer.parseInt(br.readLine());
		if (score >= 90) {
			System.out.println("A");
			
		} else if(score >= 80){
			System.out.println("B");

		} else if(score >= 70){
			System.out.println("C");

		} else if(score >= 60){
			System.out.println("D");

		} else {
			System.out.println("F");
			
		}
	}

}
