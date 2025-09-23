import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nodes = [[] for _ in range(N + 1)]
    for _ in range(M):
        p, c = map(int, input().split())
        nodes[p].append(c)
        nodes[c].append(p)

    visi = [False] * (N + 1)
    answer = 0
    for n in range(1, N + 1):
        if visi[n]:
            continue
        q = deque()
        q.append(n)
        while q:
            node = q.popleft()
            if visi[node]:
                continue
            visi[node] = True
            for nn in nodes[node]:
                if visi[nn]:
                    continue
                q.append(nn)
        answer += 1
    print(f"#{case} {answer}")