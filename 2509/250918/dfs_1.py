import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
N, K = 4, 6

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for case in range(1, T + 1):
    def dfs(x, y, token, k):
        global answer

        if k == 0:
            answer.add(token)
            return

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            dfs(nx, ny, token + board[nx][ny] * (10 ** k), k - 1)

    board = [list(map(int, input().split())) for _ in range(N)]
    answer = set()

    for i in range(N):
        for j in range(N):
            dfs(i, j, board[i][j] * (10 ** 7), K)

    print(f"#{case} {len(answer)}")