package class_B.전기차충전소;

import java.util.Scanner;

class Solution {
	private final static int MAX_N = 300;
	private final static int MAX_K = 2000;
	private final static int CMD_INIT = 100;
	private final static int CMD_ADD = 200;
	private final static int CMD_REMOVE = 300;
	private final static int CMD_COST = 400;

	private final static UserSolution usersolution = new UserSolution();

	private static boolean run(Scanner sc) {
		int q = sc.nextInt();

		int n, k;
		String strTmp;
		int[] mCostArr = new int[MAX_N];
		int[] mIdArr = new int[MAX_K];
		int[] sCityArr = new int[MAX_K];
		int[] eCityArr = new int[MAX_K];
		int[] mDistArr = new int[MAX_K];
		int mId, sCity, eCity, mDist;
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
					for (int j = 0; j < n; ++j) {
						strTmp = sc.next();
						mCostArr[j] = sc.nextInt();
					}
					for (int j = 0; j < k; ++j) {
						strTmp = sc.next();
						mIdArr[j] = sc.nextInt();
						strTmp = sc.next();
						sCityArr[j] = sc.nextInt();
						strTmp = sc.next();
						eCityArr[j] = sc.nextInt();
						strTmp = sc.next();
						mDistArr[j] = sc.nextInt();
					}
					usersolution.init(n, mCostArr, k, mIdArr, sCityArr, eCityArr, mDistArr);
					break;
				case CMD_ADD:
					strTmp = sc.next();
					mId = sc.nextInt();
					strTmp = sc.next();
					sCity = sc.nextInt();
					strTmp = sc.next();
					eCity = sc.nextInt();
					strTmp = sc.next();
					mDist = sc.nextInt();
					usersolution.add(mId, sCity, eCity, mDist);
					break;
				case CMD_REMOVE:
					strTmp = sc.next();
					mId = sc.nextInt();
					usersolution.remove(mId);
					break;
				case CMD_COST:
					strTmp = sc.next();
					sCity = sc.nextInt();
					strTmp = sc.next();
					eCity = sc.nextInt();
					strTmp = sc.next();
					ans = sc.nextInt();
					ret = usersolution.cost(sCity, eCity);
					if (ret != ans)
						okay = false;
//						System.out.println("정답 : " + ans + " 나의 답변 : " + ret);
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

		System.setIn(new java.io.FileInputStream("res/전기차충전소/sample_input.txt"));

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