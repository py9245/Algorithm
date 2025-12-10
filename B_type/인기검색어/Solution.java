import java.util.Scanner;

class Solution {
	private static Scanner sc;
    private static UserSolution userSolution = new UserSolution();

    private final static int CMD_INIT = 100;
    private final static int CMD_ADD = 200;
    private final static int CMD_TOP = 300;

    private static boolean run() throws Exception {
    	boolean okay = false;

	    int Q = sc.nextInt();

	    for (int q = 0; q < Q; q++)
	    {
	        int cmd = sc.nextInt();

	        if (cmd == CMD_INIT)
	        {
	            int N = sc.nextInt();

	            userSolution.init(N);

	            okay = true;
	        }
	        else if (cmd == CMD_ADD)
	        {
	            String mKeyword = sc.next();

	            userSolution.addKeyword(mKeyword);
	        }
	        else if (cmd == CMD_TOP)
	        {
	        	String mRet[] = new String[5];
	        	int user_ans = userSolution.top5Keyword(mRet);
	        	int correct_ans = sc.nextInt();

	        	if(correct_ans != user_ans)
	        		okay = false;

	        	for(int i=0;i<correct_ans;i++)
	        	{
	        		String ans = sc.next();
	        		if(ans.equals(mRet[i]) == false)
	        		{
	        			okay = false;
	        		}
	        	}

	        }
	    }


	    return okay;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;

        System.setIn(new java.io.FileInputStream("res/sample_input.txt"));
        sc = new Scanner(System.in);

        T = sc.nextInt();
        MARK = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }

        sc.close();
    }
}