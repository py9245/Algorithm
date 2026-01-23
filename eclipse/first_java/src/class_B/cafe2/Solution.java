package class_B.cafe2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
    private static final int CMD_INIT           = 100;
    private static final int CMD_ORDER	        = 200;
    private static final int CMD_SUPPLY			= 300;
    private static final int CMD_CANCEL			= 400;
    private static final int CMD_GET_STATUS		= 500;
    private static final int CMD_HURRY			= 600;

    private static UserSolution usersolution = new UserSolution();

    private static final int MAX_NUM_BEVERAGES = 10;

    public static class RESULT
    {
    	int cnt;
    	int[] IDs = new int[5];

    	RESULT()
    	{
    		cnt = -1;
    	}
    }

    private static boolean run(BufferedReader br) throws Exception
    {
        int Q, N, M;
        int mID, mBeverage;

        int[] mBeverages = new int[MAX_NUM_BEVERAGES];

        int ret = -1, ans, cnt;

        RESULT res;

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
                usersolution.init(N);
                okay = true;
                break;
            case CMD_ORDER:
                mID = Integer.parseInt(st.nextToken());
                M = Integer.parseInt(st.nextToken());
                for (int i = 0; i < M; ++i)
                	mBeverages[i] = Integer.parseInt(st.nextToken());
                ret = usersolution.order(mID, M, mBeverages);
                ans = Integer.parseInt(st.nextToken());
//                System.out.println("order 정답 : " + ans + " 내 답변 : " + ret);
                if (ret != ans)
                	okay = false;
                break;
            case CMD_SUPPLY:
                mBeverage =  Integer.parseInt(st.nextToken());
                ret = usersolution.supply(mBeverage);
                ans = Integer.parseInt(st.nextToken());
//                System.out.println("supply 정답 : " + ans + " 내 답변 : " + ret);
                if (ret != ans)
                	okay = false;
                break;
            case CMD_CANCEL:
                mID = Integer.parseInt(st.nextToken());
                ret = usersolution.cancel(mID);
                ans = Integer.parseInt(st.nextToken());
//                System.out.println("Calcel 정답 : " + ans + " 내 답변 : " + ret);
                if (ret != ans)
                    okay = false;
                break;
            case CMD_GET_STATUS:
            	mID = Integer.parseInt(st.nextToken());
            	ret = usersolution.getStatus(mID);
            	ans = Integer.parseInt(st.nextToken());
//            	System.out.println("get 정답 : " + ans + " 내 답변 : " + ret);
            	if (ret != ans)
            		okay = false;
            	break;
            case CMD_HURRY:
            	res = usersolution.hurry();
            	cnt = Integer.parseInt(st.nextToken());
            	if (res.cnt != cnt)
            		okay = false;
//            		System.out.println("hurry 정답 : " + cnt + " 내 답변 : " + res.cnt);
            	for (int i = 0; i < cnt; ++i)
            	{
            		ans = Integer.parseInt(st.nextToken());
            		if (res.IDs[i] != ans)
            			okay = false;
//            			System.out.println("hurry int[] 정답 : " + ans + " 내 답변 : " + res.IDs[i]);
            	}
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
        System.setIn(new java.io.FileInputStream("res/cafe2/sample_input.txt"));

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