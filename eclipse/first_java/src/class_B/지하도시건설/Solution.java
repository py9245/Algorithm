package class_B.지하도시건설;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
    private static BufferedReader br;
    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT = 1;
    private final static int CMD_DROP = 2;
    private final static int CMD_EXPLORE = 3;

    private static boolean run() throws Exception {

        StringTokenizer stdin = new StringTokenizer(br.readLine(), " ");
        int query_num = Integer.parseInt(stdin.nextToken());
        boolean ok = false;

        for (int q = 0; q < query_num; q++) {
            stdin = new StringTokenizer(br.readLine(), " ");
            int query = Integer.parseInt(stdin.nextToken());

            if (query == CMD_INIT) {
                int mH = Integer.parseInt(stdin.nextToken());
                int mW = Integer.parseInt(stdin.nextToken());
                usersolution.init(mH, mW);
                ok = true;
            } else if (query == CMD_DROP) {
                int mId = Integer.parseInt(stdin.nextToken());
                int mLen = Integer.parseInt(stdin.nextToken());
                int mExitA = Integer.parseInt(stdin.nextToken());
                int mExitB = Integer.parseInt(stdin.nextToken());
                int mCol = Integer.parseInt(stdin.nextToken());
                int ret = usersolution.dropBox(mId, mLen, mExitA, mExitB, mCol);
                int ans = Integer.parseInt(stdin.nextToken());
                if (ans != ret) {
                    ok = false;
                }
            } else if (query == CMD_EXPLORE) {
                int mIdA = Integer.parseInt(stdin.nextToken());
                int mIdB = Integer.parseInt(stdin.nextToken());
                int ret = usersolution.explore(mIdA, mIdB);
                int ans = Integer.parseInt(stdin.nextToken());
                if (ans != ret) {
                    ok = false;
                }
            }
        }
        return ok;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;

        System.setIn(new java.io.FileInputStream("res/지하도시건설/sample_input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer stinit = new StringTokenizer(br.readLine(), " ");
        T = Integer.parseInt(stinit.nextToken());
        MARK = Integer.parseInt(stinit.nextToken());

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }
        br.close();
    }
}