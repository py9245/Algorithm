import sys
sys.stdin = open("input.txt", "r")

T = int(input())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    points = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 1]
    ans = [144] * (len(points) + 1)

    def sol(arr, core, line, bd):
        if not arr:
            ans[core] = min(ans[core], line)
            return

        x, y = arr.pop()

        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            sol(arr, core + 1, line, bd)
            arr.append((x, y))
            return

        sol(arr, core, line, bd)

        for dx, dy in dxy:
            new_board = [row[:] for row in bd]
            nx, ny = x, y
            cnt = 0
            while True:
                nx += dx
                ny += dy

                if not (0 <= nx < N and 0 <= ny < N):
                    sol(arr, core + 1, line + cnt, new_board)
                    break
                if new_board[nx][ny] != 0:
                    break
                new_board[nx][ny] = 1
                cnt += 1
        arr.append((x, y))

    sol(points[:], 0, 0, board)

    for c in range(len(ans) - 1, -1, -1):
        if ans[c] != 144:
            print(f"#{test_case} {ans[c]}")
            break
