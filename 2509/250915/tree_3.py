import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(input())

for case in range(1, T + 1):

    N, M = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for _ in range(N + 2)]
    for i in range(N):
        tree[nodes[i * 2]].append(nodes[i * 2 + 1])

    q = deque([M])
    counter = set()

    while q:
        node = q.pop()
        counter.add(node)
        for n in tree[node]:
            q.append(n)
    print(f"#{case} {len(counter)}")