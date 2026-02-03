package class_B.그림판2;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;

class UserSolution
{
	static int n, l;
	static int[][] grid;

	
	static void Fill(int r, int c, int size) {
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				grid[i][j] = 1;
			}
		}
	}
	private boolean equals1(char curr, char c) {
		return curr == c;
	}
	public void init(int N, int L, char[] mCode)
	{
		n = N;
		l = L;
		grid = new int[n][n];
		
		int size = n;
//		0
//		2
		ArrayList<Integer> stack = new ArrayList<Integer>();
		int ver = 0;
		int pointX = 0;
		int pointY = 0;
		
		for (int i = 0; i < l; i++) {
			char curr = mCode[i];
//			System.out.println(curr);
			if (equals1(curr, '(')) {
				size /= 2;
				stack.add(ver);
				ver = 0;
			} else if(equals1(curr, ')')) {
				size *= 2;
				int prev = stack.remove(stack.size() - 1);

			    if (prev == 0) pointY += size;
			    else if (prev == 1) {
			        pointY -= size;
			        pointX += size;
			    }
			    else if (prev == 2) pointY += size;
			    else {
			        pointY -= size;
			        pointX -= size;
			    }

			    ver = prev + 1;
			} else {
				if(equals1(curr, '1')) {
					Fill(pointX, pointY, size);
				}
				if (ver == 0) pointY += size;
				else if(ver == 1) {
					pointY -= size;
					pointX += size;
				}
				else if(ver == 2) pointY += size;
				else  {
					pointY -= size;
					pointX -= size;
				}
				ver++;
			}
		}
//		for (int i = 0; i < n; i++) {
//			System.out.println(Arrays.toString(grid[i]));			
//		}
		return;
	}

	static int idx;
	static void EnCoding(int r, int c, int size, char[] Code) {
		int num = grid[r][c];
		boolean check = true; 
		
		for (int i = r; i < r + size; i++) {
			if (!check)break;
			for (int j = c; j < c + size; j++) {
				if(grid[i][j] != num) {check = false; break;}
			}
		}
		if(check) {
			Code[idx++] = (char) (num + 48);
			return;
		}
		Code[idx++] = '(';
		int half = size / 2;
		EnCoding(r, c, half, Code);
		EnCoding(r, c + half, half, Code);
		EnCoding(r + half, c, half, Code);
		EnCoding(r + half, c + half, half, Code);
		Code[idx++] = ')';

	}

	public int encode(char[] mCode)
	{
		idx = 0;
		EnCoding(0,0,n,mCode);
//		System.out.println(idx);
//		for (int i = 0; i < idx; i++) {
//			System.out.println(mCode[i]);
//		}
		return idx;
	}
	
	public void makeDot(int mR, int mC, int mSize, int mColor)
	{	
		for (int i = mR - mSize + 1; i < mR + mSize; i++) {
			if (i >= n)break;
			if (i < 0 )continue;
			int temp = mSize - Math.abs(i - mR);
			for (int j = mC - temp + 1; j < mC + temp; j++) {
				if (j >= n)break;
				if (j < 0 )continue;
				grid[i][j] = mColor;
				
			}
		}
		return;
	}

	static int[] DX = {0, 1, 0, -1};
	static int[] DY = {1, 0, -1, 0};
	static ArrayList<Integer> queueX;
	static ArrayList<Integer> queueY;
	
	public void paint(int mR, int mC, int mColor)
	{
		int curr = grid[mR][mC]; 
		if(curr == mColor)return;
		queueX = new ArrayList<Integer>();
		queueY = new ArrayList<Integer>();
		queueX.add(mR);
		queueY.add(mC);
		grid[mR][mC] = mColor;
		while(!queueX.isEmpty()) {
			int currX = queueX.remove(queueX.size() - 1);
			int currY = queueY.remove(queueY.size() - 1);
			
			for (int i = 0; i < 4; i++) {
				int nx = currX + DX[i];
				int ny = currY + DY[i];
				if(nx < 0 || nx >= n || ny < 0 || ny >= n || grid[nx][ny] == mColor) continue;
				grid[nx][ny] = mColor;
				queueX.add(nx);
				queueY.add(ny);
			}
		}
		
		return;
	}

	public int getColor(int mR, int mC)
	{
		return grid[mR][mC];
	}
}