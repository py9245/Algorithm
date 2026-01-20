package class_B.입시예측;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
	private static final int CMD_INIT           = 100;
	private static final int CMD_ADD	        = 200;
	private static final int CMD_ERASE 		    = 300;
	private static final int CMD_SUGGEST        = 400;

	private static UserSolution usersolution = new UserSolution();

	private static final int MAX_M = 30;

	private static int[][] mWeights = new int[MAX_M][5];

	private static boolean run(BufferedReader br) throws Exception
	{
		int Q;

		int N, M;
		int mID;
		int[] mScores = new int[5];

		int ret = -1, ans;

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		Q = Integer.parseInt(st.nextToken());

		boolean okay = false;

		for (int q = 0; q < Q; ++q)
		{
			st = new StringTokenizer(br.readLine(), " ");
			int cmd = Integer.parseInt(st.nextToken());

			switch(cmd)
			{
			case CMD_INIT:
				N = Integer.parseInt(st.nextToken());
				M = Integer.parseInt(st.nextToken());
				for (int i = 0; i < M; ++i)
				{
					st = new StringTokenizer(br.readLine(), " ");
					for (int j = 0; j < 5; ++j)
						mWeights[i][j] = Integer.parseInt(st.nextToken());
				}
				usersolution.init(N, M, mWeights);
				okay = true;
				break;
			case CMD_ADD:
				mID = Integer.parseInt(st.nextToken());
				for (int i = 0; i < 5; ++i)
					mScores[i] = Integer.parseInt(st.nextToken());
				usersolution.add(mID, mScores);
				break;
			case CMD_ERASE:
				mID = Integer.parseInt(st.nextToken());
				usersolution.erase(mID);
				break;
			case CMD_SUGGEST:
				mID = Integer.parseInt(st.nextToken());
				ret = usersolution.suggest(mID);
				ans = Integer.parseInt(st.nextToken());
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

	public static void main(String[] args) throws Exception
	{
		System.setIn(new java.io.FileInputStream("res/입시예측/sample_input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int TC = Integer.parseInt(st.nextToken());
		int MARK = Integer.parseInt(st.nextToken());

		for (int testcase = 1; testcase <= TC; ++testcase)
		{
			int score = run(br) ? MARK : 0;
			System.out.println("#" + testcase + " " + score);
		}

		br.close();
	}
}