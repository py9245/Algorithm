package class_B.음악방송;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {

    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT   = 0;
    private final static int CMD_ADD	= 1;
	private final static int CMD_REMOVE	= 2;
	private final static int CMD_GETCNT	= 3;
	
    private static boolean run(BufferedReader br) throws Exception
    {
    	int id, stime, etime;
    	int ret, ans;
 
        boolean ok = false;

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int Q = Integer.parseInt(st.nextToken());

        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine(), " ");
            int cmd = Integer.parseInt(st.nextToken());

            if (cmd == CMD_INIT) {
				stime = Integer.parseInt(st.nextToken());
				usersolution.init(stime);
                ok = true;
            } else if (cmd == CMD_ADD) {
				id = Integer.parseInt(st.nextToken());
				stime = Integer.parseInt(st.nextToken());
				etime = Integer.parseInt(st.nextToken());
				usersolution.add(id, stime, etime);
			} else if (cmd == CMD_REMOVE) {
				id = Integer.parseInt(st.nextToken());
            	usersolution.remove(id);
			} 
            else if (cmd == CMD_GETCNT) {
            	stime = Integer.parseInt(st.nextToken());
        		ret = usersolution.getCnt(stime);
        		ans = Integer.parseInt(st.nextToken());
            	if (ret != ans) {
                	ok = false;
                }
			}
			else ok = false;
        }
        return ok;
    }

    public static void main(String[] args) throws Exception {

        System.setIn(new java.io.FileInputStream("res/음악방송/sample_input.txt"));
        
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer line = new StringTokenizer(br.readLine(), " ");

        int T = Integer.parseInt(line.nextToken());
        int MARK = Integer.parseInt(line.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            int score = run(br) ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }

        br.close();
    }
}