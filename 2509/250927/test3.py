import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = int(input())

for tc in range(1 ,T + 1):
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            if px > py:
                px, py = py, px
            parents[py] = px

    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    answer = f"#{tc} "
    for _ in range(M):
        cmd, a, b = map(int,input().split())
        if not cmd:
            union(a,b)
        else:
            answer += "1" if find(a) == find(b) else "0"
    print(answer)