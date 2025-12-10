import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

import heapq

T = int(input())

for case in range(1, T + 1):
    N, M, X = map(int, input().split())
    linked = [[] for _ in range(N + 1)]
    for _ in range(M):
        p, b, c = map(int, input().split())
        linked[p].append([c, b])

    s_to_e_dist = [0] * (N + 1)
    for n in range(1, N + 1):
        hq = []
        dist = [float('inf')] * (N + 1)
        dist[n] = 0
        heapq.heappush(hq, [0, n])

        while hq:
            cd, cn = heapq.heappop(hq)

            if cn == X:
                s_to_e_dist[n] = cd
                break

            if cd > dist[cn]:
                continue

            for d, node in linked[cn]:
                nd = d + cd
                if nd >= dist[node]:
                    continue
                heapq.heappush(hq, [nd, node])
                dist[node] = nd


    e_to_s_dist = [float('inf')] * (N + 1)
    e_to_s_dist[X] = 0
    hq = []
    heapq.heappush(hq, [0, X])

    while hq:
        cd, cn = heapq.heappop(hq)

        if cd > e_to_s_dist[cn]:
            continue

        for d, node in linked[cn]:
            nd = d + cd
            if nd >= e_to_s_dist[node]:
                continue
            heapq.heappush(hq, [nd, node])
            e_to_s_dist[node] = nd
    answer_list = [s_to_e_dist[i] + e_to_s_dist[i] for i in range(1, N + 1)]

    print(f"#{case} {max(answer_list)}")