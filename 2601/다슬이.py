import sys

sys.stdin = open("input.txt", "r")

class SegBeats:

    def __init__(self, a):

        self.INF = 4 * 10**18

        m = len(a)

        self.n = 1

        while self.n < m:

            self.n <<= 1

        self.mn = [self.INF] * (self.n << 1)

        self.mn2 = [self.INF] * (self.n << 1)

        self.cnt = [0] * (self.n << 1)

        for i in range(m):

            self.mn[self.n + i] = a[i]

            self.cnt[self.n + i] = 1

        for i in range(self.n - 1, 0, -1):

            self.pull(i)

 

    def pull(self, i):

        l, r = i << 1, i << 1 | 1

        if self.mn[l] < self.mn[r]:

            self.mn[i] = self.mn[l]

            self.cnt[i] = self.cnt[l]

            self.mn2[i] = min(self.mn2[l], self.mn[r])

        elif self.mn[l] > self.mn[r]:

            self.mn[i] = self.mn[r]

            self.cnt[i] = self.cnt[r]

            self.mn2[i] = min(self.mn2[r], self.mn[l])

        else:

            self.mn[i] = self.mn[l]

            self.cnt[i] = self.cnt[l] + self.cnt[r]

            self.mn2[i] = min(self.mn2[l], self.mn2[r])

 

    def apply_node(self, i, v):

        if self.mn[i] >= v:

            return 0

        self.mn[i] = v

        return self.cnt[i]

 

    def push(self, i):

        l, r = i << 1, i << 1 | 1

        v = self.mn[i]

        if self.mn[l] < v < self.mn2[l]:

            self.mn[l] = v

        if self.mn[r] < v < self.mn2[r]:

            self.mn[r] = v

 

    def chmax_dfs(self, i, tl, tr, ql, qr, v):

        if qr <= tl or tr <= ql or self.mn[i] >= v:

            return 0

        if ql <= tl and tr <= qr and v < self.mn2[i]:

            return self.apply_node(i, v)

        if tr - tl == 1:

            return self.apply_node(i, v)

        self.push(i)

        tm = (tl + tr) >> 1

        res = self.chmax_dfs(i << 1, tl, tm, ql, qr, v)

        res += self.chmax_dfs(i << 1 | 1, tm, tr, ql, qr, v)

        self.pull(i)

        return res

 

    def chmax(self, l, r, v):

        if l >= r:

            return 0

        return self.chmax_dfs(1, 0, self.n, l, r, v)

 

def main():

    T = int(input())

    for tc in range(1, T + 1):

        N = int(input())

        root_sal = int(input())

 

        parent = [-1] * (N + 1)

        salary = [0] * (N + 1)

        salary[0] = root_sal

 

        hires = [(0, -1)] * (N + 1)

        g = [[] for _ in range(N + 1)]

 

        for i in range(1, N + 1):

            s, p = map(int, input().split())

            salary[i] = s

            parent[i] = p

            hires[i] = (s, p)

            g[p].append(i)

 

        # HLD 준비

        sz = [0] * (N + 1)

        heavy = [-1] * (N + 1)

        stack = [(0, 0)]

        while stack:

            u, state = stack.pop()

            if state == 0:

                stack.append((u, 1))

                for v in g[u]:

                    stack.append((v, 0))

            else:

                best = -1

                mx = 0

                total = 1

                for v in g[u]:

                    total += sz[v]

                    if sz[v] > mx:

                        mx = sz[v]

                        best = v

                sz[u] = total

                heavy[u] = best

 

        head = [0] * (N + 1)

        pos = [0] * (N + 1)

        order = []

        stack = [(0, 0)]

        while stack:

            u, h = stack.pop()

            v = u

            while v != -1:

                head[v] = h

                pos[v] = len(order)

                order.append(v)

                for w in g[v]:

                    if w != heavy[v]:

                        stack.append((w, w))

                v = heavy[v]

 

        base = [salary[v] for v in order]

        seg = SegBeats(base)

 

        ans = 0

        root_head = head[0]

 

        for i in range(1, N + 1):

            s, u = hires[i]

            while u != -1 and head[u] != root_head:

                h = head[u]

                ans += seg.chmax(pos[h], pos[u] + 1, s)

                u = parent[h]

            if u != -1:

                ans += seg.chmax(pos[0], pos[u] + 1, s)

 

        print(f"#{tc} {ans}")

 

if __name__ == "__main__":

    main()