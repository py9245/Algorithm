package class_B.경유지운송;

import java.util.Scanner;

class Solution {
	private final static int MAX_E = 2000;
	private final static int MAX_S = 3;
	private final static int CMD_INIT = 100;
	private final static int CMD_ADD = 200;
	private final static int CMD_CALC = 300;

	private final static UserSolution usersolution = new UserSolution();

	private static boolean run(Scanner sc) {
		int q = sc.nextInt();

		int n, m, k;
		String strTmp;
		int[] sCityArr = new int[MAX_E];
		int[] eCityArr = new int[MAX_E];
		int[] mLimitArr = new int[MAX_E];
		int[] mStopover = new int[MAX_S];
		int sCity, eCity, mLimit;
		int cmd, ans, ret = 0;
		boolean okay = false;

		for (int i = 0; i < q; ++i) {
			cmd = sc.nextInt();
			strTmp = sc.next();
			switch (cmd) {
				case CMD_INIT:
					okay = true;
					strTmp = sc.next();
					n = sc.nextInt();
					strTmp = sc.next();
					k = sc.nextInt();
					for (int j = 0; j < k; ++j) {
						strTmp = sc.next();
						sCityArr[j] = sc.nextInt();
						strTmp = sc.next();
						eCityArr[j] = sc.nextInt();
						strTmp = sc.next();
						mLimitArr[j] = sc.nextInt();
					}
					usersolution.init(n, k, sCityArr, eCityArr, mLimitArr);
					break;
				case CMD_ADD:
					strTmp = sc.next();
					sCity = sc.nextInt();
					strTmp = sc.next();
					eCity = sc.nextInt();
					strTmp = sc.next();
					mLimit = sc.nextInt();
					usersolution.add(sCity, eCity, mLimit);
					break;
				case CMD_CALC:
					strTmp = sc.next();
					sCity = sc.nextInt();
					strTmp = sc.next();
					eCity = sc.nextInt();
					strTmp = sc.next();
					m = sc.nextInt();
					for (int j = 0; j < m; ++j) {
						strTmp = sc.next();
						mStopover[j] = sc.nextInt();
					}
					strTmp = sc.next();
					ans = sc.nextInt();
					ret = usersolution.calculate(sCity, eCity, m, mStopover);
					if (ret != ans)
						okay = false;
					break;
				default:
					okay = false;
					break;
			}
		}
		return okay;
	}

	public static void main(String[] args) throws Exception {
		int TC, MARK;

		System.setIn(new java.io.FileInputStream("res/경유지운송/sample_input.txt"));

		Scanner sc = new Scanner(System.in);

		TC = sc.nextInt();
		MARK = sc.nextInt();

		for (int testcase = 1; testcase <= TC; ++testcase) {
			int score = run(sc) ? MARK : 0;
			System.out.println("#" + testcase + " " + score);
		}

		sc.close();
	}
}