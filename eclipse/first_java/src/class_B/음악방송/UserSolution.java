package class_B.음악방송;

import java.util.HashMap;

class UserSolution {

    static final int MAXT = 2_000_000 + 5;

    int musicTime;

    static class Emp {
        int s, b; // valid start interval [s, b]
        Emp(int s, int b) { this.s = s; this.b = b; }
    }

    HashMap<Integer, Emp> map;
    int[] bit;

    void init(int musicTime) {
        this.musicTime = musicTime;
        this.map = new HashMap<>(8192);
        this.bit = new int[MAXT];
    }

    void add(int mID, int mStart, int mEnd) {
        Emp old = map.get(mID);
        if (old != null) {
            rangeAdd(old.s, old.b, -1);
        }

        int b = mEnd - musicTime;
        if (b < mStart) { // 안전장치(문제 조건상 거의 없음)
            map.put(mID, new Emp(mStart, mStart - 1));
            return;
        }

        Emp neu = new Emp(mStart, b);
        map.put(mID, neu);
        rangeAdd(neu.s, neu.b, +1);
    }

    void remove(int mID) {
        Emp old = map.remove(mID);
        if (old == null) return;
        if (old.b >= old.s) rangeAdd(old.s, old.b, -1);
    }
//그냥 구간만 기록
    int getCnt(int mBSTime) {
        return pointQuery(mBSTime);
    }

    void rangeAdd(int l, int r, int delta) {
        addBIT(l, delta);
        addBIT(r + 1, -delta);
    }

    void addBIT(int idx, int delta) {
        for (int i = idx + 1; i < MAXT; i += (i & -i)) {
            bit[i] += delta;
        }
    }

    int pointQuery(int idx) {
        int sum = 0;
        for (int i = idx + 1; i > 0; i -= (i & -i)) {
            sum += bit[i];
        }
        return sum;
    }
}
