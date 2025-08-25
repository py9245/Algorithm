import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
rg = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    rg[b].append(a)

def bfs(start, bd):
    vis = [False] * (N + 1)
    q = deque([start])
    vis[start] = True
    cnt = 0
    while q:
        x = q.popleft()
        for nx in bd[x]:
            if not vis[nx]:
                vis[nx] = True
                q.append(nx)
                cnt += 1
    return cnt

ans = 0
for i in range(1, N + 1):
    ta = bfs(i, g)
    shor = bfs(i, rg)
    if ta + shor == N - 1:
        ans += 1

print(ans)