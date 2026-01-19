package class_B.파일공유;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {

	private static UserSolution userSolution = new UserSolution();

	private final static int CMD_INIT     	= 100;
	private final static int CMD_MAKENET    = 200;
	private final static int CMD_ADDLINK    = 300;
	private final static int CMD_SHARED     = 400;
	private final static int CMD_DOWNLOAD   = 500;
	private final static int CMD_GETSIZE    = 600;
	
	private final static int MAX_COM = 1000;
	private final static int MAX_ONEFILE = 50;

	private static int fileCnt[] = new int[MAX_COM];
	private static int fileID[][] = new int[MAX_COM][MAX_ONEFILE];
	private static int fileSize[][] = new int[MAX_COM][MAX_ONEFILE];
	
	private static int comA[] = new int[MAX_COM * 2];
	private static int comB[] = new int[MAX_COM * 2];
	private static int Dis[] = new int[MAX_COM * 2];
	
	private static boolean run(BufferedReader br) throws Exception
	{
		boolean ok = false;

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int Q = Integer.parseInt(st.nextToken());
		for (int q = 0; q < Q; q++) {
			st = new StringTokenizer(br.readLine(), " ");
            int cmd = Integer.parseInt(st.nextToken());

			if (cmd == CMD_INIT) {
				int N = Integer.parseInt(st.nextToken());
				for (int i = 0; i < N; i++) {
					st = new StringTokenizer(br.readLine(), " ");
					fileCnt[i] = Integer.parseInt(st.nextToken());
					for (int k = 0; k < fileCnt[i]; k++) {
						fileID[i][k] = Integer.parseInt(st.nextToken());
						fileSize[i][k] = Integer.parseInt(st.nextToken());
					}
				}
				userSolution.init(N, fileCnt, fileID, fileSize);
				ok = true;
			}
			else if (cmd == CMD_MAKENET) {
				int K = Integer.parseInt(st.nextToken());
				for (int i = 0; i < K; i++) {
					st = new StringTokenizer(br.readLine(), " ");
					comA[i] = Integer.parseInt(st.nextToken());
					comB[i] = Integer.parseInt(st.nextToken());
					Dis[i] = Integer.parseInt(st.nextToken());
				}
				userSolution.makeNet(K, comA, comB, Dis);
			}
			else if (cmd == CMD_ADDLINK) {
				int time = Integer.parseInt(st.nextToken());
				int com1 = Integer.parseInt(st.nextToken());
				int com2 = Integer.parseInt(st.nextToken());
				int dis = Integer.parseInt(st.nextToken());
				userSolution.addLink(time, com1, com2, dis);
			}
			else if (cmd == CMD_SHARED) {
				int time = Integer.parseInt(st.nextToken());
				int com1 = Integer.parseInt(st.nextToken());
				int id = Integer.parseInt(st.nextToken());
				int size = Integer.parseInt(st.nextToken());
				userSolution.addShareFile(time, com1, id, size);
			}
			else if(cmd == CMD_DOWNLOAD) {
				int time = Integer.parseInt(st.nextToken());
				int com1 = Integer.parseInt(st.nextToken());
				int id = Integer.parseInt(st.nextToken());
				int ans = Integer.parseInt(st.nextToken());
				int ret = userSolution.downloadFile(time, com1, id);
				if(ans != ret) {
					ok = false;
				}
			}
			else if(cmd == CMD_GETSIZE) {
				int time = Integer.parseInt(st.nextToken());
				int com1 = Integer.parseInt(st.nextToken());
				int id = Integer.parseInt(st.nextToken());
				int ans = Integer.parseInt(st.nextToken());
				int ret = userSolution.getFileSize(time, com1, id);
				if(ans != ret) {
					ok = false;
				}
			}
			else ok = false;
		}

		return ok;
	}

	public static void main(String[] args) throws Exception {

		//System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

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