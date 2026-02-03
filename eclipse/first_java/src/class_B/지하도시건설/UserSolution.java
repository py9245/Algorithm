package class_B.지하도시건설;

import java.util.ArrayList;
import java.util.HashMap;

class UserSolution {

	static int h, w, currW;
	static final int HASH = 200_000;
	
	static class Space{
		int mID, s, e, row;
		Space(int mID, int s, int e, int row) {this.mID = mID; this.s = s; this.e = e; this.row = row;}
	}
	static HashMap<Integer, int[]>
	
	static ArrayList<Space>[] space;
	
	public void init(int mH, int mW) {
		h = mH;
		w = mW;
		currW = w - 1;
		space = new ArrayList[h];
		for (int i = 0; i < h; i++) {
			space[i] = new ArrayList<Space>();
		}
		
	}

	public int dropBox(int mId, int mLen, int mExitA, int mExitB, int mCol) {
		return 0;
	}

	public int explore(int mIdA, int mIdB) {
		return -1;
	}

}