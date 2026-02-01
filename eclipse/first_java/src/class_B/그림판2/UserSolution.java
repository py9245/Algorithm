package class_B.그림판2;

import java.util.Arrays;

class UserSolution
{

	static int n, l;
//	static int k;
	static int[]grid;
	static boolean[][] check;
	static void deCoding(char[] mCode) {
		
	}
	
	static StringBuilder sb;
	static int answer;
	static boolean inCoding(int s, int e) {
		if (s == e) {
			return (grid[s] == 0)? false : true;
		}
		int zero = s;
		int firs = e / 4;
		int seco = e / 3;
		int thre = e / 2;
		int four = e / 1;
		
		boolean firsC = inCoding(zero, firs);
		boolean secoC = inCoding(firs, seco);
		boolean threC = inCoding(seco, thre);
		boolean fourC = inCoding(thre, four);
		
		if(firsC && secoC && threC && fourC) {
			sb.append(1);
			return true;
		}
		else {
			sb.append("(");
			sb.append((firsC == true)? 1:0);
			sb.append((secoC == true)? 1:0);
			sb.append((threC == true)? 1:0);
			sb.append((fourC == true)? 1:0);
			sb.append(")");
			return false;
		}
	}
	
	public void init(int N, int L, char[] mCode)
	{
		n = N;
		l = L;
		
		grid = new int[(n * n) + 1];
		
		
//		k = 1;
//		int temp = 2;
//		while (temp < n) {
//			temp *= 2;
//			k++;
//		}
//		check = new boolean[k + 1][];
//		for (int i = 0; i <= k; i++) {
//			int tempP = (int)Math.pow(2, i);
//			check[i] = new boolean[tempP * tempP];
//			Arrays.fill(check[i], true);
//		}

		return;
	}

	public int encode(char[] mCode)
	{
		sb = new StringBuilder();
		sb.append("\"");
		if (inCoding(1, n * n))return
		sb.append("\"");
		return -1;
	}

	public void makeDot(int mR, int mC, int mSize, int mColor)
	{
		return;
	}

	public void paint(int mR, int mC, int mColor)
	{
		return;
	}

	public int getColor(int mR, int mC)
	{
		return -1;
	}
}