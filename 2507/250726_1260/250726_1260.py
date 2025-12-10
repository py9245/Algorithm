import sys
from collections import deque

input = input = sys.stdin.readline

N, M, V = map(int, input().split())
gr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

for g in gr:
    g.sort()

visited = [False] * (N + 1)
dfs_p = []

def dfs(v):
    visited[v] = True
    dfs_p.append(v)
    for nxt in gr[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(V)

bfs_p = []
visited = [False] * (N + 1)
q = deque([V])
visited[V] = True

while q:
    v = q.popleft()
    bfs_p.append(v)
    for nxt in gr[v]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

print(*dfs_p)
print(*bfs_p)