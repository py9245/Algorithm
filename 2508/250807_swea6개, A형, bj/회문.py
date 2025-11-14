T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    m = M//2
    def sol():
        for idx in range(N):
            for jdx in range(N - M + 1):
                for dx in range(m):
                    if not(board[idx][jdx + dx] == board[idx][jdx + (M - dx - 1)]):
                        break
                else:
                    print(f"#{case} {''.join(board[idx][jdx + i] for i in range(M))}")
                    return
                for dx in range(m):
                    if not (board[jdx + dx][idx] == board[jdx + (M - dx - 1)][idx]):
                        break
                else:
                    print(f"#{case} {''.join(board[jdx + i][idx] for i in range(M))}")
                    return
    sol()