import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    highest = max(map(max, board))
    start_idx = [(i, j) for i in range(N) for j in range(N) if board[i][j] == highest]
    best = 0
    end_if = False

    def dfs(x, y, tr, total):
        global best, end_if
        visited[x][y] = True

        if total > best:
            best = total

            if best == N * N:
                end_if = True
                visited[x][y] = False
                return

        num = board[x][y]

        for dx, dy in dxy:
            if end_if:
                return
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue

            n_num = board[nx][ny]

            if num > n_num:
                dfs(nx, ny, tr, total + 1)
            elif n_num - K < num and tr:
                board[nx][ny] = num - 1
                dfs(nx, ny, False, total + 1)
                board[nx][ny] = n_num
        visited[x][y] = False


    for i, j in start_idx:
        dfs(i, j, True, 1)

    print(f"#{case} {best}")