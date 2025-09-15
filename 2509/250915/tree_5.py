import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = 10

for case in range(1, T + 1):

    class Tree:
        def __init__(self, n):
            self.n = n
            self.tree = [None, None, None] * (n * 2)
            self.answer = ''

        def link_node(self, node, nxt):
            if not self.tree[node][0]:
                self.tree[node][0] = nxt
            else:
                self.tree[node][1] = nxt


        def solve(self, node=1):
            if self.tree[node][1]:
                self.solve(self.tree[node][1])
            self.answer += self.tree[node][0]
            if self.tree[node][2]:
                self.solve(self.tree[node][2])



    N = int(input())
    tree = Tree(N)

    for _ in range(N):
        a = input().split()
        idx = int(a[0])
        value = a[1]
        if len(a) == 3:
            tree.tree[idx] = (value, int(a[2]), None)
        elif len(a) == 4:
            tree.tree[idx] = (value, int(a[2]), int(a[3]))
        else:
            tree.tree[idx] = (value, None, None)

    tree.solve()
    print(f"{case} {tree.answer}")

