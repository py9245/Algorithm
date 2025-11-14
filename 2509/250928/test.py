import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())

for tc in range(1 ,T + 1):
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(min_root, max_root):

        if min_root != max_root:
            if min_root > max_root:
                min_root, max_root = max_root, min_root
            parents[max_root] = min_root


    N, M = map(int, input().split())
    parents = list(range(N + 1))
    root = [list(map(int, input().split())) for _ in range(M)]
    root.sort(key=lambda x : x[2])
    answer = 0
    for a, b, c in root:
        fx, fy = find(a), find(b)
        if fx == fy:
            continue
        answer += c
        union(a, b)

    for i in range(1, N + 1):
        find(i)

    print(f"#{tc} {answer}")


