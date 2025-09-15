import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(input())

for case in range(1, T + 1):
    class Tree:
        def __init__(self, n):
            self.n = n
            self.arr = [0] * (n + 1)

        def setting(self, idx, val):
            self.arr[idx] = val

        def solve(self, idx):
            if idx > self.n:
                return 0
            total = self.arr[idx]

            return total + self.solve(idx * 2) + self.solve(idx * 2 + 1)

    N, M, L = map(int, input().split())
    bi_tree = Tree(N)
    for _ in range(M):
        i, v = map(int, input().split())
        bi_tree.setting(i, v)
    print(f"#{case} {bi_tree.solve(L)}")