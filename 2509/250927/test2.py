import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

T = 10

for tc in range(1, T + 1):
    def dfs(n):
        global answer
        if n > N:
            return

        degree = len(tree[n])

        if degree > 1:
            dfs(int(tree[n][1]))
        answer += tree[n][0]
        if degree > 2:
            dfs(int(tree[n][2]))
        return

    N = int(input())
    tree = [None] + [list(input().split())[1::] for _ in range(N)]
    answer = ''
    dfs(1)
    print(f"#{tc} {answer}")




