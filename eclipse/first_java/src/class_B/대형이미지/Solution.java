package class_B.대형이미지;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {

	private static UserSolution userSolution = new UserSolution();

	private final static int CMD_INIT     = 100;
	private final static int CMD_ADD      = 200;
	private final static int CMD_PRESS    = 300;
	private final static int CMD_GET      = 400;

	private static int pixel[][] = new int[10000][3];

	private static boolean run(BufferedReader br) throws Exception
	{
		boolean ok = false;

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int Q = Integer.parseInt(st.nextToken());
		for (int q = 0; q < Q; q++) {
			st = new StringTokenizer(br.readLine(), " ");
            int cmd = Integer.parseInt(st.nextToken());

			if (cmd == CMD_INIT) {
				int N = Integer.parseInt(st.nextToken());
				userSolution.init(N);
				ok = true;
			}
			else if (cmd == CMD_ADD) {
				int id = Integer.parseInt(st.nextToken());
				int size = Integer.parseInt(st.nextToken());
				int cnt = Integer.parseInt(st.nextToken());
				for (int i = 0; i < cnt; i++) {
					st = new StringTokenizer(br.readLine(), " ");
					pixel[i][0] = Integer.parseInt(st.nextToken());
					pixel[i][1] = Integer.parseInt(st.nextToken());
					pixel[i][2] = Integer.parseInt(st.nextToken());
				}
				userSolution.addPrint(id, size, cnt, pixel);
			}
			else if (cmd == CMD_PRESS) {
				int id = Integer.parseInt(st.nextToken());
				int row = Integer.parseInt(st.nextToken());
				int col = Integer.parseInt(st.nextToken());
				int dir = Integer.parseInt(st.nextToken());
				userSolution.pressPrint(id, row, col, dir);
			}
			else if(cmd == CMD_GET) {
				int row = Integer.parseInt(st.nextToken());
				int col = Integer.parseInt(st.nextToken());
				int ans = Integer.parseInt(st.nextToken());
				int ret = userSolution.getDepth(row, col);
				if(ans != ret) {
					ok = false;
//					System.out.println("정답 : " + ans + " 내 답변 : " + ret);
				}
			}
			else ok = false;
		}

		return ok;
	}

	public static void main(String[] args) throws Exception {

		System.setIn(new java.io.FileInputStream("res/대형이미지/sample_input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer line = new StringTokenizer(br.readLine(), " ");

		int T = Integer.parseInt(line.nextToken());
		int MARK = Integer.parseInt(line.nextToken());

		for (int tc = 1; tc <= T; tc++) {
			int score = run(br) ? MARK : 0;
			System.out.println("#" + tc + " " + score);
		}

		br.close();
	}
}