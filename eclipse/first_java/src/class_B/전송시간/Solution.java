package class_B.전송시간;

import java.util.Scanner;


class Solution {
    private static Scanner sc;
    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT   = 0;
    private final static int CMD_ADD    = 1;
	private final static int CMD_REMOVE = 2;
	private final static int CMD_CHECK  = 3;
	
	private final static int MAX_LINE = 30000;
	
	private static int nodeA[] = new int[MAX_LINE];
	private static int nodeB[] = new int[MAX_LINE];
	private static int Time[] = new int[MAX_LINE];	
	
    private static boolean run() throws Exception
    {
    	int cmd, N, K;
    	int ans, ret;
 
        boolean ok = false;

        int Q = sc.nextInt();
        for (int q = 0; q < Q; q++) {
            cmd = sc.nextInt();

            if (cmd == CMD_INIT) {
            	N = sc.nextInt();
            	K = sc.nextInt();
    			for (int i = 0; i < K; i++) {
    				nodeA[i] = sc.nextInt();
    				nodeB[i] = sc.nextInt();
    				Time[i] = sc.nextInt();
    			}
    			usersolution.init(N, K, nodeA, nodeB, Time);
    			ok = true;
            } else if (cmd == CMD_ADD) {
            	nodeA[0] = sc.nextInt();
            	nodeB[0] = sc.nextInt();
            	Time[0] = sc.nextInt();
				usersolution.addLine(nodeA[0], nodeB[0], Time[0]);
			} else if (cmd == CMD_REMOVE) {
				nodeA[0] = sc.nextInt();
            	nodeB[0] = sc.nextInt();
				usersolution.removeLine(nodeA[0], nodeB[0]);
			} else if (cmd == CMD_CHECK) {
				nodeA[0] = sc.nextInt();
				nodeB[0] = sc.nextInt();
				ans = sc.nextInt();
				ret = usersolution.checkTime(nodeA[0], nodeB[0]);
				if (ans != ret) {
					ok = false;
				}
			}
			else ok = false;
        }
        return ok;
    }

    public static void main(String[] args) throws Exception {

        System.setIn(new java.io.FileInputStream("res/전송시간/sample_input.txt"));
        sc = new Scanner(System.in);

        int T = sc.nextInt();
        int MARK = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }

        sc.close();
    }
}