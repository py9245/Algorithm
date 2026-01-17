package class_B.커피점제과점;

import java.util.Scanner;

class Solution {
	private final static int MAX_E = 30000;
	private final static int MAX_SHOP = 1000;
	private final static int CMD_INIT = 100;
	private final static int CMD_ADD = 200;
	private final static int CMD_CALC = 300;

	private final static UserSolution usersolution = new UserSolution();

	private static boolean run(Scanner sc) {
		int q = sc.nextInt();

		int n, k, m, p, r;
		int[] sBuildingArr = new int[MAX_E];
		int[] eBuildingArr = new int[MAX_E];
		int[] mDistArr = new int[MAX_E];
		int[] mCoffee = new int[MAX_SHOP];
		int[] mBakery = new int[MAX_SHOP];
		int sBuilding, eBuilding, mDist;
		int cmd, ans, ret = 0;
		boolean okay = false;

		for (int i = 0; i < q; ++i) {
			cmd = sc.nextInt();
			switch (cmd) {
				case CMD_INIT:
					okay = true;
					n = sc.nextInt();
					k = sc.nextInt();
					for (int j = 0; j < MAX_E; ++j) {
						sBuildingArr[j] = -1;
						eBuildingArr[j] = -1;
						mDistArr[j] = 0;
					}
					for (int j = 0; j < k; ++j) {
						sBuildingArr[j] = sc.nextInt();
						eBuildingArr[j] = sc.nextInt();
						mDistArr[j] = sc.nextInt();
					}
					usersolution.init(n, k, sBuildingArr, eBuildingArr, mDistArr);
					break;
				case CMD_ADD:
					sBuilding = sc.nextInt();
					eBuilding = sc.nextInt();
					mDist = sc.nextInt();
					usersolution.add(sBuilding, eBuilding, mDist);
					break;
				case CMD_CALC:
					m = sc.nextInt();
					p = sc.nextInt();
					r = sc.nextInt();
					for (int j = 0; j < MAX_SHOP; ++j) {
						mCoffee[j] = -1;
						mBakery[j] = -1;
					}
					for (int j = 0; j < m; ++j) {
						mCoffee[j] = sc.nextInt();
					}
					for (int j = 0; j < p; ++j) {
						mBakery[j] = sc.nextInt();
					}
					ret = usersolution.calculate(m, mCoffee, p, mBakery, r);
					ans = sc.nextInt();
					if (ans != ret)
						okay =false;
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

		//System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

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