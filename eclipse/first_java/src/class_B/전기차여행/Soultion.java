package class_B.전기차여행;

import java.util.Scanner;

class Solution {
	private final static int MAX_N = 500;
	private final static int MAX_M = 5;
	private final static int MAX_K = 4000;
	private final static int CMD_INIT = 100;
	private final static int CMD_ADD = 200;
	private final static int CMD_REMOVE = 300;
	private final static int CMD_COST = 400;

	private final static UserSolution usersolution = new UserSolution();

	private static boolean run(Scanner sc) {
		int q = sc.nextInt();

		int n, m, k, b;
		int[] mChargeArr = new int[MAX_N];
		int[] mIdArr = new int[MAX_K];
		int[] sCityArr = new int[MAX_K];
		int[] eCityArr = new int[MAX_K];
		int[] mTimeArr = new int[MAX_K];
		int[] mPowerArr = new int[MAX_K];
		int[] mCityArr = new int[MAX_M];
		int mId, sCity, eCity, mTime, mPower;
		int cmd, ans, ret = 0;
		boolean okay = false;

		for (int i = 0; i < q; ++i) {
			cmd = sc.nextInt();
			switch (cmd) {
				case CMD_INIT:
					okay = true;
					n = sc.nextInt();
					k = sc.nextInt();
					for (int j = 0; j < n; ++j) {
						mChargeArr[j] = sc.nextInt();
					}
					for (int j = 0; j < k; ++j) {
						mIdArr[j] = sc.nextInt();
						sCityArr[j] = sc.nextInt();
						eCityArr[j] = sc.nextInt();
						mTimeArr[j] = sc.nextInt();
						mPowerArr[j] = sc.nextInt();;
					}
					usersolution.init(n, mChargeArr, k, mIdArr, sCityArr, eCityArr, mTimeArr, mPowerArr);
					break;
				case CMD_ADD:
					mId = sc.nextInt();
					sCity = sc.nextInt();
					eCity = sc.nextInt();
					mTime = sc.nextInt();
					mPower = sc.nextInt();
					usersolution.add(mId, sCity, eCity, mTime, mPower);
					break;
				case CMD_REMOVE:
					mId = sc.nextInt();
					usersolution.remove(mId);
					break;
				case CMD_COST:
					b = sc.nextInt();
					sCity = sc.nextInt();
					eCity = sc.nextInt();
					ans = sc.nextInt();
					m = sc.nextInt();
					for (int j = 0; j < m; ++j) {
						mCityArr[j] = sc.nextInt();
						mTimeArr[j] = sc.nextInt();
					}
					ret = usersolution.cost(b, sCity, eCity, m, mCityArr, mTimeArr);
					if (ans != ret)
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

		System.setIn(new java.io.FileInputStream("res/전기차여행/sample_input.txt"));

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