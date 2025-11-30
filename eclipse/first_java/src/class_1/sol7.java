package class_1;

import java.io.*;
import java.util.StringTokenizer;

public class sol7 {

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("res/input7.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;
        final int N = 5;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			answer += num * num;
		}
        System.out.println(answer % 10);
    }

}
