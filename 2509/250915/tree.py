import sys
from collections import deque
sys.stdin = open('input.txt', "r")

# T = int(input())


class Tree:
    def __init__(self, n):
        self.n = n
        self.tree = [[0, 0] for _ in range(n + 1)]

    def link_node(self, node, nxt):
        if not self.tree[node][0]:
            self.tree[node][0] = nxt
        else:
            self.tree[node][1] = nxt

    def perorder(self, node=1):
        print(node, end=" ")
        if self.tree[node][0]:
            self.perorder(self.tree[node][0])
        if self.tree[node][1]:
            self.perorder(self.tree[node][1])


    def inorder(self, node=1):
        if self.tree[node][0]:
            self.inorder(self.tree[node][0])
        print(node, end=" ")
        if self.tree[node][1]:
            self.inorder(self.tree[node][1])

    def postorder(self, node=1):
        if self.tree[node][0]:
            self.postorder(self.tree[node][0])
        if self.tree[node][1]:
            self.postorder(self.tree[node][1])
        print(node, end=" ")


N = int(input())
nodes = list(map(int, input().split()))
tree = Tree(N)

for i in range(len(nodes)//2):
    a, b = nodes[i * 2], nodes[i * 2 + 1]
    tree.link_node(a, b)

tree.perorder()
print()
tree.inorder()
print()
tree.postorder()
print()
