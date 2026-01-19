package class_B.파일공유;

import java.util.ArrayList;

class UserSolution {
	
	static int n, k;
	static long lastTime;
	
	static class File{
		int fId, size;
		
		public File(int fId, int size) {
			this.fId = fId;
			this.size = size;
		}
	}
	
	static ArrayList<File>[] files;
	
	static class Edge {
		int node, weight;
		
		public Edge(int node, int weight) {
			this.node = node;
			this.weight = weight;
		}
	}
	
	static ArrayList<Edge>[] link;
	
	static void update(int updateTime) {
		
	}
	
	static class Task implements Comparable<Task>{
		int toID, fromID, endTime, totalSize;
		File
	}
	
	static void bfs(int node) {
		
	}
	
	void init(int N, int mShareFileCnt[], int mFileID[][], int mFileSize[][])
	{
		n = N;
		files = new ArrayList[N + 1];
		for (int i = 0; i < N; i++) {
			files[i] = new ArrayList<File>();
			for (int j = 0; j < mShareFileCnt[i]; j++) {
				files[i + 1].add(new File(mFileID[i][j], mFileSize[i][j]));
			}
		}
	}

	void makeNet(int K, int mComA[], int mComB[], int mDis[])
	{	
		k = K;
		link = new ArrayList[n + 1];
		for (int i = 0; i < n + 1; i++) {
			link[i] = new ArrayList<Edge>();
		}
		int a, b, c;
		for (int i = 0; i < K; i++) {
			a = mComA[i];
			b = mComB[i];
			c = mDis[i];
			link[a].add(new Edge(b, c));
			link[b].add(new Edge(a, c));
		}
	}

	void addLink(int mTime, int mComA, int mComB, int mDis)
	{
		link[mComA].add(new Edge(mComB, mDis));
		link[mComB].add(new Edge(mComA, mDis));
		update(mTime);
	}

	void addShareFile(int mTime, int mComA, int mFileID, int mSize)
	{
		files[mComA].add(new File(mFileID, mSize));
		update(mTime);
	}

	int downloadFile(int mTime, int mComA, int mFileID)
	{
		update(mTime);
		return 0;
	}

	int getFileSize(int mTime, int mComA, int mFileID)
	{
		update(mTime);
		return 0;
	}
}