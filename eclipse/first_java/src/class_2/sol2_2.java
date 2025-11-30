package class_2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class sol2_2 {

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input2.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		final int size = 6;
		int[] sizeArr = new int[size];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++) {
			sizeArr[i] = Integer.parseInt(st.nextToken());
		}
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		int clothes = Integer.parseInt(st2.nextToken());
		int pen = Integer.parseInt(st2.nextToken());
		int answer = 0;
		for (int i : sizeArr) {
			answer += (i + clothes - 1) / clothes;
		}
		System.out.println(answer);
		System.out.println(N/pen + " " + N%pen);
	}

}
