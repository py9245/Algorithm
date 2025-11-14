import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

import heapq

T = int(input())

for tc in range(1, T + 1):
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y, d):
        global answer, cnt

        px, py = find(x), find(y)
        if px != py:
            answer += d
            cnt += 1
            if rank[px] > rank[py]:
                parents[px] = py
            elif rank[px] < rank[py]:
                parents[py] = px
            else:
                parents[py] = px
                rank[px] += 1

    N, M = map(int, input().split())
    parents = [ i for i in range(N + 1)]
    rank = [0] * (N + 1)
    tree = [list(map(int, input().split())) for _ in range(M)]
    tree.sort(key=lambda x : x[2])
    answer = 0
    cnt = 0
    for A, B, C in tree:
        if cnt == N - 1:
            break
        union(A, B, C)
    print(f"#{tc} {answer}")

