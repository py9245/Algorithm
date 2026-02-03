package class_B.지하도시건설;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.TreeSet;

class UserSolution {

	static int h, w, currW;
	static final int HASH = 200_000;
	static final int MAXID = 10_001;
	
	static class Box implements Comparable<Box>{
		int mID, s, e, row, len;
		int[] can;
		Box(int mID, int s, int e, int row) {this.mID = mID; this.s = s; this.e = e; this.row = row;}
		public int compareTo(Box o) {
			return this.s - o.s;
		}
	}
	static TreeSet<Box>[] box;
	
	static Box[] boxinfo;

//	헤쉬맵으로 경로압축키에 들어갈 수 있는
	static HashMap<Integer, int[]> edge;
	
	public void init(int mH, int mW) {
		h = mH;
		w = mW;
		currW = w - 1;
		boxinfo = new Box[MAXID];
		box = new TreeSet[h];
		for (int i = 0; i < h; i++) {
			box[i] = new TreeSet<Box>();
		}
		edge = new HashMap<Integer, int[]>();
				
	}

	public int dropBox(int mId, int mLen, int mExitA, int mExitB, int mCol) {
		int prevRow = -1;
		for (int i = currW; i < h; i++) {
			boolean check = true;
			int currS = i * HASH + mCol;
			int currE = currS + mLen - 1;
			if(box[i].isEmpty()) {
				prevRow = i;
				continue;
			}
			for (Box curr : box[i]) {
				if(curr.s > currE)break;
				if(curr.e > currS || curr.s > currS) {
					check = false;
					break;
				}
			}
			if (check) {
				prevRow = i;
			} else if(prevRow > 0) {
				break;
			}
		}
		return 0;
	}

	public int explore(int mIdA, int mIdB) {
		return -1;
	}

}