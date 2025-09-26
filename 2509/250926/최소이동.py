import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

import heapq

T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    linked = [[] for _ in range(M)]
    for _ in range(M):
        p, b, c = map(int, input().split())
        linked[p].append([c, b])
    dist = [float('inf')] * (N + 1)
    dist[0] = 0
    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cd, node = heapq.heappop(pq)

        if node == N:
            break

        if cd > dist[node]:
            continue

        for d, nn in linked[node]:
            nd = cd + d
            if nd >= dist[nn]:
                continue
            heapq.heappush(pq, [nd, nn])
            dist[nn] = nd
    print(f"#{case} {dist[-1]}")