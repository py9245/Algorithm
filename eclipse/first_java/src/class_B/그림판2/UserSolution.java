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
				ver = stack.remove(stack.size() - 1) + 1;
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
		for (int i = 0; i < n; i++) {
			System.out.println(Arrays.toString(grid[i]));			
		}
		return;
	}

	private boolean equals(char curr, char c) {
		// TODO Auto-generated method stub
		return false;
	}

	public int encode(char[] mCode)
	{
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