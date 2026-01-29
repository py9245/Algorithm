package class_B.전송시간;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class UserSolution {
	 
    static int n, k, nCnt;
 
    static class Edge {
        int v, w, num;
        Edge(int v, int w) {
            this.v = v;
            this.w = w;
            this.num = v % 100;
        }
    }
 
    static class Node implements Comparable<Node> {
        int v, w, num;
        public Node(int v, int w, int num) {
            this.v = v;
            this.w = w;
            this.num = num;
        }
        public int compareTo(Node o) {
            return Integer.compare(this.w, o.w);
        }
    }
 
    static PriorityQueue<Node> pq;
    static final int INF = 1_000_000_000;
 
    static ArrayList<Edge>[] smalledge;
    static ArrayList<Edge>[] largeedge;
 
    static int[][][] smalldist;
    static int[][] largedist;
 
    static Edge[][][] intra;
 
    static boolean dirty;
    static int dirtyGroup;
 
    static boolean isLargeEdge(int a, int b) {
        if (a <= 3 || b <= 3) return true;
        return (a / 100) != (b / 100);
    }
 
    static void recomputeGroup(int g) {
        for (int start = 1; start <= 3; start++) {
            Arrays.fill(smalldist[g][start], INF);
            pq = new PriorityQueue<>();
            pq.add(new Node(g * 100 + start, 0, start));
            smalldist[g][start][start] = 0;
 
            while (!pq.isEmpty()) {
                Node curr = pq.poll();
                if (smalldist[g][start][curr.num] < curr.w) continue;
 
                for (Edge next : smalledge[curr.v]) {
                    int nextW = curr.w + next.w;
                    if (smalldist[g][start][next.num] <= nextW) continue;
                    smalldist[g][start][next.num] = nextW;
                    pq.add(new Node(next.v, nextW, next.num));
                }
            }
        }
    }
 
    static void updateIntraEdges(int g) {
        intra[g][1][2].w = smalldist[g][1][2];
        intra[g][1][3].w = smalldist[g][1][3];
 
        intra[g][2][1].w = smalldist[g][2][1];
        intra[g][2][3].w = smalldist[g][2][3];
 
        intra[g][3][1].w = smalldist[g][3][1];
        intra[g][3][2].w = smalldist[g][3][2];
    }
 
    static void dijkstraLarge(int root) {
        Arrays.fill(largedist[root], INF);
        pq = new PriorityQueue<>();
        pq.add(new Node(root, 0, 0));
        largedist[root][root] = 0;
 
        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            if (largedist[root][curr.v] < curr.w) continue;
 
            for (Edge next : largeedge[curr.v]) {
                if (next.w >= INF) continue;
                int nextW = curr.w + next.w;
                if (largedist[root][next.v] <= nextW) continue;
                largedist[root][next.v] = nextW;
                pq.add(new Node(next.v, nextW, next.num));
            }
        }
    }
 
    static void recomputeLargeAll() {
        for (int r = 1; r <= 3; r++) dijkstraLarge(r);
    }
 
    static void update() {
        if (!dirty) return;
 
        if (dirtyGroup != 0) {
            recomputeGroup(dirtyGroup);
            updateIntraEdges(dirtyGroup);
        }
 
        recomputeLargeAll();
 
        dirty = false;
        dirtyGroup = 0;
    }
 
    @SuppressWarnings("unchecked")
    public void init(int N, int K, int mNodeA[], int mNodeB[], int mTime[]) {
        n = N;
        nCnt = 100 * n + 31;
        k = K;
 
        smalledge = new ArrayList[nCnt];
        largeedge = new ArrayList[nCnt];
        for (int i = 0; i < nCnt; i++) {
            smalledge[i] = new ArrayList<>();
            largeedge[i] = new ArrayList<>();
        }
 
        smalldist = new int[n + 1][4][31];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < 4; j++) {
                Arrays.fill(smalldist[i][j], INF);
            }
        }
 
        largedist = new int[4][nCnt];
        for (int i = 0; i < 4; i++) Arrays.fill(largedist[i], INF);
 
        intra = new Edge[n + 1][4][4];
 
        for (int i = 0; i < k; i++) {
            int a = mNodeA[i], b = mNodeB[i], w = mTime[i];
            if (isLargeEdge(a, b)) {
                largeedge[a].add(new Edge(b, w));
                largeedge[b].add(new Edge(a, w));
            } else {
                smalledge[a].add(new Edge(b, w));
                smalledge[b].add(new Edge(a, w));
            }
        }
 
        for (int g = 1; g <= n; g++) {
            recomputeGroup(g);
 
            int base = g * 100;
 
            Edge e12 = new Edge(base + 2, smalldist[g][1][2]);
            Edge e13 = new Edge(base + 3, smalldist[g][1][3]);
            Edge e21 = new Edge(base + 1, smalldist[g][2][1]);
            Edge e23 = new Edge(base + 3, smalldist[g][2][3]);
            Edge e31 = new Edge(base + 1, smalldist[g][3][1]);
            Edge e32 = new Edge(base + 2, smalldist[g][3][2]);
 
            intra[g][1][2] = e12; largeedge[base + 1].add(e12);
            intra[g][1][3] = e13; largeedge[base + 1].add(e13);
 
            intra[g][2][1] = e21; largeedge[base + 2].add(e21);
            intra[g][2][3] = e23; largeedge[base + 2].add(e23);
 
            intra[g][3][1] = e31; largeedge[base + 3].add(e31);
            intra[g][3][2] = e32; largeedge[base + 3].add(e32);
        }
 
        recomputeLargeAll();
 
        dirty = false;
        dirtyGroup = 0;
    }
 
    public void addLine(int mNodeA, int mNodeB, int mTime) {
        if (isLargeEdge(mNodeA, mNodeB)) {
            largeedge[mNodeA].add(new Edge(mNodeB, mTime));
            largeedge[mNodeB].add(new Edge(mNodeA, mTime));
 
            dirty = true;
            dirtyGroup = 0;
        } else {
            smalledge[mNodeA].add(new Edge(mNodeB, mTime));
            smalledge[mNodeB].add(new Edge(mNodeA, mTime));
 
            dirty = true;
            dirtyGroup = mNodeA / 100;
        }
        update();
    }
 
    public void removeLine(int mNodeA, int mNodeB) {
        boolean removed = false;
 
        if (isLargeEdge(mNodeA, mNodeB)) {
            for (int i = 0; i < largeedge[mNodeA].size(); i++) {
                if (largeedge[mNodeA].get(i).v == mNodeB) {
                    largeedge[mNodeA].remove(i);
                    removed = true;
                    break;
                }
            }
            for (int i = 0; i < largeedge[mNodeB].size(); i++) {
                if (largeedge[mNodeB].get(i).v == mNodeA) {
                    largeedge[mNodeB].remove(i);
                    removed = true;
                    break;
                }
            }
 
            if (removed) {
                dirty = true;
                dirtyGroup = 0;
                update();
            }
        } else {
            for (int i = 0; i < smalledge[mNodeA].size(); i++) {
                if (smalledge[mNodeA].get(i).v == mNodeB) {
                    smalledge[mNodeA].remove(i);
                    removed = true;
                    break;
                }
            }
            for (int i = 0; i < smalledge[mNodeB].size(); i++) {
                if (smalledge[mNodeB].get(i).v == mNodeA) {
                    smalledge[mNodeB].remove(i);
                    removed = true;
                    break;
                }
            }
 
            if (removed) {
                dirty = true;
                dirtyGroup = mNodeA / 100;
                update();
            }
        }
    }
 
    public int checkTime(int mNodeA, int mNodeB) {
        return largedist[mNodeA][mNodeB];
    }
}