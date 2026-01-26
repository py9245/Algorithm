package class_B.온라인마트;

import java.util.*;

class UserSolution {

    static final int IDXLEN = 31;

    static int[] sellCnt;
    static int[] sellDis;

    static class Sell {
        int sID, cate, comp, hash;
        int adjusted;     // ✅ mPrice + startDis
        boolean isDone;

        Sell(int sID, int cate, int comp, int price, int hash) {
            this.sID = sID;
            this.cate = cate;
            this.comp = comp;
            this.hash = hash;
            this.adjusted = price + sellDis[hash]; // ✅ startDis 포함
            this.isDone = false;
        }
    }

    static class Node implements Comparable<Node> {
        int sID, hash, adjusted;

        Node(Sell s) {
            this.sID = s.sID;
            this.hash = s.hash;
            this.adjusted = s.adjusted;
        }

        @Override
        public int compareTo(Node o) {
            if (this.adjusted != o.adjusted) return this.adjusted - o.adjusted;
            return this.sID - o.sID;
        }
    }

    // show 후보용 (실제 현재가격 기준으로 비교)
    static class Cand implements Comparable<Cand> {
        int hash, sID, curPrice;

        Cand(int hash, int sID, int curPrice) {
            this.hash = hash;
            this.sID = sID;
            this.curPrice = curPrice;
        }

        @Override
        public int compareTo(Cand o) {
            if (this.curPrice != o.curPrice) return this.curPrice - o.curPrice;
            return this.sID - o.sID;
        }
    }

    static HashMap<Integer, Integer> sellHashs;  // mID -> hash
    static HashMap<Integer, Sell>[] sellInfo;    // hash별 mID -> Sell
    static PriorityQueue<Node>[] PQ;             // ✅ hash별 PQ

    static int getHash(int cate, int comp) {
        return cate * 5 + comp;
    }

    public void init() {
        sellCnt = new int[IDXLEN];
        sellDis = new int[IDXLEN];

        sellHashs = new HashMap<>();
        sellInfo = new HashMap[IDXLEN];
        PQ = new PriorityQueue[IDXLEN];

        for (int i = 0; i < IDXLEN; i++) {
            sellInfo[i] = new HashMap<>();
            PQ[i] = new PriorityQueue<>();
        }
    }

    // ✅ hash PQ의 top이 유효해질 때까지 정리 (판매종료/할인으로 죽은 상품 제거)
    private void purge(int hash) {
        while (!PQ[hash].isEmpty()) {
            Node top = PQ[hash].peek();
            Sell s = sellInfo[hash].get(top.sID);

            if (s == null || s.isDone) {
                PQ[hash].poll();
                continue;
            }

            // ✅ 현재 가격 = adjusted - sellDis[hash]
            if (s.adjusted - sellDis[hash] <= 0) {
                PQ[hash].poll();
                if (!s.isDone) {
                    s.isDone = true;
                    sellCnt[hash]--;
                }
                continue;
            }

            return;
        }
    }

    public int sell(int mID, int mCategory, int mCompany, int mPrice) {
        int hash = getHash(mCategory, mCompany);

        sellCnt[hash]++;
        sellHashs.put(mID, hash);

        Sell curr = new Sell(mID, mCategory, mCompany, mPrice, hash);
        sellInfo[hash].put(mID, curr);

        PQ[hash].add(new Node(curr));
        return sellCnt[hash];
    }

    public int closeSale(int mID) {
        Integer hashObj = sellHashs.get(mID);
        if (hashObj == null) return -1;
        int hash = hashObj;

        Sell s = sellInfo[hash].get(mID);
        if (s == null || s.isDone) return -1;

        // 할인으로 이미 죽어야 하는데 purge 안된 경우 대비
        if (s.adjusted - sellDis[hash] <= 0) {
            s.isDone = true;
            sellCnt[hash]--;
            return -1;
        }

        s.isDone = true;
        sellCnt[hash]--;

        return s.adjusted - sellDis[hash];
    }

    public int discount(int mCategory, int mCompany, int mAmount) {
        int hash = getHash(mCategory, mCompany);

        sellDis[hash] += mAmount;

        // ✅ 전체 순회 절대 X : 죽는 애들만 PQ top에서 제거
        purge(hash);

        return sellCnt[hash];
    }

    Solution.RESULT show(int mHow, int mCode) {
        Solution.RESULT res = new Solution.RESULT();
        res.IDs = new int[5];

        PriorityQueue<Cand> candPQ = new PriorityQueue<>();
        ArrayList<Node>[] popped = new ArrayList[IDXLEN];
        for (int i = 0; i < IDXLEN; i++) popped[i] = new ArrayList<>();

        // 후보 hash들만 top을 넣는다
        if (mHow == 0) {
            for (int cate = 1; cate <= 5; cate++) {
                for (int comp = 1; comp <= 5; comp++) {
                    int h = getHash(cate, comp);
                    purge(h);
                    if (!PQ[h].isEmpty()) {
                        Node top = PQ[h].peek();
                        int cur = top.adjusted - sellDis[h];
                        candPQ.add(new Cand(h, top.sID, cur));
                    }
                }
            }
        } else if (mHow == 1) {
            int cate = mCode;
            for (int comp = 1; comp <= 5; comp++) {
                int h = getHash(cate, comp);
                purge(h);
                if (!PQ[h].isEmpty()) {
                    Node top = PQ[h].peek();
                    int cur = top.adjusted - sellDis[h];
                    candPQ.add(new Cand(h, top.sID, cur));
                }
            }
        } else {
            int comp = mCode;
            for (int cate = 1; cate <= 5; cate++) {
                int h = getHash(cate, comp);
                purge(h);
                if (!PQ[h].isEmpty()) {
                    Node top = PQ[h].peek();
                    int cur = top.adjusted - sellDis[h];
                    candPQ.add(new Cand(h, top.sID, cur));
                }
            }
        }

        int cnt = 0;
        while (!candPQ.isEmpty() && cnt < 5) {
            Cand c = candPQ.poll();
            int h = c.hash;

            purge(h);
            if (PQ[h].isEmpty()) continue;

            Node realTop = PQ[h].poll();
            popped[h].add(realTop);

            Sell s = sellInfo[h].get(realTop.sID);
            if (s == null || s.isDone) continue;

            // 다시 한번 안전 체크
            int curPrice = s.adjusted - sellDis[h];
            if (curPrice <= 0) continue;

            res.IDs[cnt++] = s.sID;

            purge(h);
            if (!PQ[h].isEmpty()) {
                Node nxt = PQ[h].peek();
                int cur = nxt.adjusted - sellDis[h];
                candPQ.add(new Cand(h, nxt.sID, cur));
            }
        }

        // PQ 복구
        for (int h = 0; h < IDXLEN; h++) {
            for (Node n : popped[h]) PQ[h].add(n);
        }

        res.cnt = cnt;
        return res;
    }
}
