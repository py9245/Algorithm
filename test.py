import sys

sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for case in range(1, T + 1):
    N = int(input())
    x, y = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    num = board[x][y]

    for i in range(N):
        for j in range(N):
            if board[i][j] >= num:
                board[i][j] = num
            if board[i][j] < 1:
                board[i][j] = 1
    total = 0
    while True:
        num = board[x][y]
        total += 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and num > board[nx][ny]:
                x, y = nx, ny
                break
        else:
            break

    print(f"#{case} {total}")