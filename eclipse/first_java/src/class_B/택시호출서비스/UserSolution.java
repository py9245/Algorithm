package class_B.택시호출서비스;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.PriorityQueue;

class UserSolution
{
	static int n, m, l;
	static int[] ver;
	static class Texi implements Comparable<Texi>{
		int mID, x, y, allMove, move, ver;
		
		public Texi(int mID, int x, int y) {
			this.mID = mID;
			this.x = x;
			this.y = y;
		}
		
		public int compareTo(Texi o) {
			if (this.move != o.move) return o.move - this.move;
			return this.mID - o.mID;
		}
	}
	static Texi[] texi;
	static PriorityQueue<Texi> rank;
	
	static final int GRIDSIZE = 100;
	static HashMap<Integer, ArrayList<Integer>>[] grid;
	
	static int getBucketIdx(int x, int y) {
		return (x / l) * 10 + (y / l);
	}
	
	static int[] gridIdx = new int[2];
	static void getIdx(int hash) {
		gridIdx[0] = hash / n;
		gridIdx[1] = hash % n;
	}
	
	static final int[] DX = {0, 10, -10};
	static final int[] DY = {0, 1, -1};
	
	public void init(int N, int M, int L, int[] mXs, int[] mYs)
	{	
		n = N;
		m = M;
		l = L;
		texi = new Texi[M + 1];
		rank = new PriorityQueue<Texi>();
		grid = new HashMap[GRIDSIZE];
		for (int i = 0; i < GRIDSIZE; i++) {
			grid[i] = new HashMap<Integer, ArrayList<Integer>>();
		}
		
		int x, y, hash;
		
		for (int i = 0; i < M; i++) {
			x = mXs[i];
			y = mYs[i];
			Texi curr = new Texi(i + 1, x, y);
			curr.ver = 0;
			texi[i+1] = curr;
			rank.add(curr);
			hash = x * N + y;
			int bucketIdx = getBucketIdx(x, y);
			if (grid[bucketIdx].getOrDefault(hash, null) == null) {
				grid[bucketIdx].put(hash, new ArrayList<Integer>());
			}
			grid[bucketIdx].get(hash).add(i + 1);
		}
		
		return;
	}

	static int getDist(int sx, int sy, int ex, int ey) {
		return Math.abs(sx - ex) + Math.abs(sy - ey);
	}
	
	public int pickup(int mSX, int mSY, int mEX, int mEY)
	{
		int minDist = l + 1;
		int minTexi = m + 1;
		int minBucketIdx = 0;
		int minkey = 0;
		int minidx = 0;
		int bucketIdx = getBucketIdx(mSX, mSY);
		
		for (int i = 0; i < DX.length; i++) {
			for (int j = 0; j < DY.length; j++) {
				int BI = bucketIdx + DX[i] + DY[j];
				if (BI < 0 || BI >= GRIDSIZE) continue;
				for (Integer key : grid[BI].keySet()) {
					getIdx(key);
					int cx = gridIdx[0];
					int cy = gridIdx[1];
					int cDist = getDist(mSX, mSY, cx, cy);
					if(cDist > minDist) continue;
					ArrayList<Integer> temp = grid[BI].get(key);
					Collections.sort(temp, (o1, o2) -> o2 - o1);
					if(cDist == minDist && minTexi < temp.get(temp.size() - 1)) continue;
					minDist = cDist;
					minTexi = temp.get(temp.size() - 1);
					minBucketIdx = BI;
					minkey = key;
					minidx = temp.size() - 1; 
				}
			}
		}
		if (minDist == l + 1) return -1;
		int toEnd = getDist(mSX, mSY, mEX, mEY);
		ArrayList<Integer> list = grid[minBucketIdx].get(minkey);
		list.remove(minidx);
		if (list.isEmpty()) grid[minBucketIdx].remove(minkey);

		
		int b2 = getBucketIdx(mEX, mEY);
		int key2 = mEX * n + mEY;
		ArrayList<Integer> temp = grid[b2].get(key2);
		if (temp == null) {
		    temp = new ArrayList<>();
		    grid[b2].put(key2, temp);
		}
		temp.add(minTexi);

		Texi prev = texi[minTexi];

		Texi nt = new Texi(minTexi, mEX, mEY);
		nt.allMove = prev.allMove + minDist + toEnd;
		nt.move    = prev.move + toEnd;
		nt.ver     = prev.ver + 1;

		texi[minTexi] = nt;
		rank.add(nt);

		
		return minTexi;
	}

	public Solution.Result reset(int mNo)
	{
		Solution.Result res = new Solution.Result();
		res.mX = texi[mNo].x;
		res.mY = texi[mNo].y;
		res.mMoveDistance = texi[mNo].allMove;
		res.mRideDistance = texi[mNo].move;
		Texi nt = new Texi(mNo, texi[mNo].x, texi[mNo].y);
		nt.allMove = 0;
		nt.move = 0;
		nt.ver = texi[mNo].ver + 1;
		texi[mNo] = nt;
		rank.add(nt);
		return res;
	}

	public void getBest(int[] mNos)
	{	
		int cnt = 0;
		Texi curr;
		Texi[] ranking = new Texi[5];
		
		while (cnt < 5 && !rank.isEmpty()) {
			curr = rank.poll();
			if (curr.ver != texi[curr.mID].ver) continue;
			ranking[cnt++] = curr;
		}
		
		for (int i = 0; i < ranking.length; i++) {
			if(ranking[i] == null) break;
			mNos[i] = ranking[i].mID;
			rank.add(ranking[i]);
		}
		return;
	}
}


//N 은 10의 배수
//도시 내에 택시들 M개 1 ~ M
//출발지부터 거리 L 이하 중 가까운 거리(가장 가까운 것 많으면 택시번호 작은것)
//L은 언제나 N / 10