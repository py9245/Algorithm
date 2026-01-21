package class_B.서비스센터;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
	private static BufferedReader br;
    private static UserSolution userSolution = new UserSolution();

    private final static int CMD_INIT       = 100;
    private final static int CMD_RECEIVE    = 200;
    private final static int CMD_ADD        = 300;
    private final static int CMD_REMOVE     = 400;
    private final static int CMD_EVAL       = 500;
    
    private static boolean run() throws Exception {
    	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N, M, mTime, mId, rId, mWorkload, mGrade, mThroughput, ret, ans;
    	
        int Q = Integer.parseInt(st.nextToken());
    	boolean okay = false;

	    for (int q = 0; q < Q; ++q)
	    {
        	st = new StringTokenizer(br.readLine(), " ");
	        int cmd = Integer.parseInt(st.nextToken());

	        if (cmd == CMD_INIT)
	        {
	            N = Integer.parseInt(st.nextToken());
	            M = Integer.parseInt(st.nextToken());
	            userSolution.init(N, M);
	            okay = true;
	        }
	        else if (cmd == CMD_RECEIVE)
	        {
                mTime = Integer.parseInt(st.nextToken());
                mId = Integer.parseInt(st.nextToken());
                mWorkload = Integer.parseInt(st.nextToken());
                mGrade = Integer.parseInt(st.nextToken());
	            userSolution.receive(mTime, mId, mWorkload, mGrade);
	        }
	        else if (cmd == CMD_ADD)
	        {
                mTime = Integer.parseInt(st.nextToken());
                rId = Integer.parseInt(st.nextToken());
                mThroughput = Integer.parseInt(st.nextToken());
	            userSolution.add(mTime, rId, mThroughput);
	        	
	        }
	        else if(cmd == CMD_REMOVE)
	        {
                mTime = Integer.parseInt(st.nextToken());
                rId = Integer.parseInt(st.nextToken());
                ans = Integer.parseInt(st.nextToken());
	            ret = userSolution.remove(mTime, rId);
//	            System.out.println("re정답 : " + ans + "내 답변: " + ret);
                if(ans != ret)
	        		okay = false;
	        }
	        else if(cmd == CMD_EVAL)
	        {
                mTime = Integer.parseInt(st.nextToken());
                mGrade = Integer.parseInt(st.nextToken());
                ans = Integer.parseInt(st.nextToken());
	            ret = userSolution.evaluate(mTime, mGrade);
//	            System.out.println("ev정답 : " + ans + "내 답변: " + ret);
                if(ans != ret)
	        		okay = false;
	        }
	    }
	    return okay;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;

        System.setIn(new java.io.FileInputStream("res/서비스센터/sample_input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));        
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        T = Integer.parseInt(st.nextToken());
        MARK = Integer.parseInt(st.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }

        br.close();
    }
}