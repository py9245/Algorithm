package class_B.그림판2;

import java.util.Scanner;

class Solution
{	
	private static final int CMD_INIT 				= 100;
	private static final int CMD_ENCODE				= 200;
	private static final int CMD_MAKE_DOT			= 300;
	private static final int CMD_PAINT		 		= 400;
	private static final int CMD_GET_COLOR			= 500;
	
    private static UserSolution usersolution = new UserSolution();

    private static char[] mCode = new char[200001];
    private static char[] aCode = new char[200001];
    
    static int mstrncmp(char[] a, char[] b, int n)
    {
    	for (int i = 0; i < n; ++i)
    		if (a[i] != b[i])
    			return a[i] - b[i];
    	return 0;
    }

    static void readcode(Scanner sc, int L, char code[]) throws Exception
    {
    	for (int i = 0; i < L;)
    	{
    		String buf = sc.next();
    		for (int j = 0; j < buf.length(); ++j)
    			code[i++] = buf.charAt(j);
    	}
    	code[L] = '\0';
    }
    
    private static boolean run(Scanner sc) throws Exception 
    {
    	int Q, N, L;
    	int mR, mC, mSize, mColor;

    	int ret = -1, ans;

    	Q = sc.nextInt();

    	boolean okay = false;

    	for (int q = 0; q < Q; ++q)
    	{
    		int cmd = sc.nextInt();

    		switch(cmd)
    		{
    		case CMD_INIT:
    			N = sc.nextInt();
    			L = sc.nextInt();
    			readcode(sc, L, mCode);
    			usersolution.init(N, L, mCode);
    			okay = true;
    			break;
    		case CMD_ENCODE:
    			ret = usersolution.encode(mCode);
    			ans = sc.nextInt();
    			readcode(sc, ans, aCode);
    			if (ret != ans || mstrncmp(mCode, aCode, ans) != 0)
    				okay = false;
    			break;
    		case CMD_MAKE_DOT:
    			mR = sc.nextInt();
    			mC = sc.nextInt();
    			mSize = sc.nextInt();
    			mColor = sc.nextInt();
    			usersolution.makeDot(mR, mC, mSize, mColor);
    			break;
    		case CMD_PAINT:
    			mR = sc.nextInt();
    			mC = sc.nextInt();
    			mColor = sc.nextInt();
    			usersolution.paint(mR, mC, mColor);
    			break;
    		case CMD_GET_COLOR:
    			mR = sc.nextInt();
    			mC = sc.nextInt();
    			ret = usersolution.getColor(mR, mC);
    			ans = sc.nextInt();
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
        System.setIn(new java.io.FileInputStream("res/그림판2/sample_input.txt"));

		Scanner sc = new Scanner(System.in);
		
		int TC = sc.nextInt();
        int MARK = sc.nextInt();
        
        for (int testcase = 1; testcase <= TC; ++testcase)
        {
			int score = run(sc) ? MARK : 0;
            System.out.println("#" + testcase + " " + score);
        }

        sc.close();
        
    }
}