N, M = map(int, input().split())
board = [input() for _ in range(N)]
max_size = min(N, M)

for size in range(max_size - 1, -1, -1):
    for i in range(N - size):
        for j in range(M - size):
            if board[i][j] == board[i+size][j] == board[i][j+size] == board[i+size][j+size]:
                print((size + 1) ** 2)
                exit()

print(1)