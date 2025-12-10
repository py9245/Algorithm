import sys

sys.stdin = open("input.txt", "r")

class segment:
    def init(self, N):
        self.n = N
        self.arr = []
        self.create_arr()
        self.tree = [0] * (self.n * 4)
        self.create_tree(1, 0, self.n - 1)

    def create_arr(self):
        for _ in range(self.n):
            self.arr.append(int(input()))

    def create_tree(self, node, s, e):
        if s == e:
            self.tree[node] = self.arr[s]
            # print(f"node : {node} s : {s}")
            return
        mid = (s + e) // 2
        self.create_tree(node * 2, s, mid)
        self.create_tree(node * 2 + 1, mid + 1, e)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
        # print(f"node : {node} {self.tree[node]} // node * 2 : {node * 2} {self.tree[node * 2]} // node * 2 + 1 : {node * 2 + 1} {self.tree[node * 2 + 1]}")

    def query(self, node, s, e, l, r):
        if r < s or e < l:  # 겹치지 않음
            return 0
        if l <= s and e <= r:  # 완전히 포함
            return self.tree[node]
        m = (s + e) // 2
        return self.query(node * 2, s, m, l, r) + \
               self.query(node * 2 + 1, m + 1, e, l, r)

    def update(self, node, s, e, idx, val):
        if s == e:
            self.arr[idx] = val
            self.tree[node] = val
            return
        m = (s + e) // 2
        if idx <= m:
            self.update(node * 2, s, m, idx, val)
        else:
            self.update(node * 2 + 1, m + 1, e, idx, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

N, M, K = map(int, input().split())

sol = segment()
sol.init(N)

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        sol.update(1, 0, N - 1, b - 1, c)
    else:
        print(sol.query(1, 0, N - 1, b - 1, c - 1))



