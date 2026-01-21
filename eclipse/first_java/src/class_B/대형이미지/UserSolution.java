package class_B.대형이미지;

import java.util.HashMap;

class UserSolution {

    static class Image {
        int size;
        int stride;          // size + 1
        int[][] prefix4;     // prefix4[dir] = (size+1)*(size+1) 1D prefix sum

        Image(int size) {
            this.size = size;
            this.stride = size + 1;
            this.prefix4 = new int[4][];
        }
    }

    static class Press {
        Image img;
        int row, col, dir;
        Press(Image img, int row, int col, int dir) {
            this.img = img;
            this.row = row;
            this.col = col;
            this.dir = dir;
        }
    }

    static int N;
    static HashMap<Integer, Image> images;

    static Press[] presses;
    static int pressCnt;

    void init(int N) {
        UserSolution.N = N;
        images = new HashMap<>(64);

        presses = new Press[5000];
        pressCnt = 0;
    }

    void addPrint(int mID, int mSize, int mCnt, int[][] mPixel) {
        Image img = new Image(mSize);
        int S = mSize;
        int stride = img.stride;

        // dir별로 (S+1)*(S+1) prefix 배열 만들기
        for (int dir = 0; dir < 4; dir++) {
            int[] pref = new int[stride * stride]; // [0..S][0..S] (1D)
            // 값 채우기: 원래 좌표 (r,c)를 회전시킨 (rr,cc)에 p를 놓는다.
            for (int i = 0; i < mCnt; i++) {
                int r = mPixel[i][0];
                int c = mPixel[i][1];
                int p = mPixel[i][2];

                int rr, cc;
                if (dir == 0) {                // 그대로
                    rr = r; cc = c;
                } else if (dir == 1) {         // CCW 90
                    rr = S - 1 - c; cc = r;
                } else if (dir == 2) {         // 180
                    rr = S - 1 - r; cc = S - 1 - c;
                } else {                        // dir == 3, CCW 270 (CW 90)
                    rr = c; cc = S - 1 - r;
                }

                // prefix는 1-based로 값 배치: (rr+1, cc+1)
                pref[(rr + 1) * stride + (cc + 1)] = p;
            }

            // 2D prefix sum 만들기 (in-place)
            // pref[i][j] = val + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]
            for (int i = 1; i <= S; i++) {
                int base = i * stride;
                int up = (i - 1) * stride;
                int rowSum = 0;
                for (int j = 1; j <= S; j++) {
                    int idx = base + j;
                    rowSum += pref[idx];          // val 누적
                    pref[idx] = rowSum + pref[up + j]; // 위쪽 prefix 더함
                }
            }

            img.prefix4[dir] = pref;
        }

        images.put(mID, img);
    }

    void pressPrint(int mID, int mRow, int mCol, int mDir) {
        Image img = images.get(mID);
        presses[pressCnt++] = new Press(img, mRow, mCol, mDir);
    }

    int getDepth(int mRow, int mCol) {
        int ans = 0;

        // 보드 윈도우: [mRow..mRow+24], [mCol..mCol+24]
        int winR1 = mRow;
        int winC1 = mCol;
        int winR2 = mRow + 24;
        int winC2 = mCol + 24;

        for (int i = 0; i < pressCnt; i++) {
            Press pr = presses[i];
            Image img = pr.img;

            int S = img.size;
            int stride = img.stride;
            int[] pref = img.prefix4[pr.dir];

            // 이 press가 찍힌 보드 좌표 = (pr.row + rr, pr.col + cc)
            // 윈도우와 겹치는 이미지 내부 좌표 범위를 구한다.
            int r1 = winR1 - pr.row;
            int c1 = winC1 - pr.col;
            int r2 = winR2 - pr.row;
            int c2 = winC2 - pr.col;

            // 이미지 범위 [0..S-1]와 교집합
            if (r2 < 0 || c2 < 0 || r1 >= S || c1 >= S) continue;

            if (r1 < 0) r1 = 0;
            if (c1 < 0) c1 = 0;
            if (r2 >= S) r2 = S - 1;
            if (c2 >= S) c2 = S - 1;

            // 2D prefix로 직사각형 합 O(1)
            // sum = P(r2+1,c2+1) - P(r1,c2+1) - P(r2+1,c1) + P(r1,c1)
            int A = (r2 + 1) * stride + (c2 + 1);
            int B = (r1) * stride + (c2 + 1);
            int C = (r2 + 1) * stride + (c1);
            int D = (r1) * stride + (c1);

            ans += pref[A] - pref[B] - pref[C] + pref[D];
        }

        return ans;
    }
}
