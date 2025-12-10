T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 0
    for i in range(N):
        for j in range(M):
            total = board[i][j]
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    total += board[nx][ny]
            ans = max(ans, total)
    print(f"#{case} {ans}")