import sys, time
st = time.time()
sys.stdin = open('input.txt', "r")

T = int(input())

for case in range(1, T + 1):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    sp = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                sp.append((i, j))

    best_answer = len(sp)
    answer = 0

    for k in range(N + 2, 0, -1):
        cost = k * k + (k - 1) * (k - 1)
        if cost > M * best_answer or cost < answer:
            continue
        for x in range(N):
            for y in range(N):
                total = 0
                nk = k - 1
                for dx in range(-nk, nk + 1):
                    nx = x + dx
                    if nx < 0:
                        continue
                    if nx == N:
                        break
                    rem = nk - abs(dx)
                    total += sum(board[nx][max(0, y - rem):min(N, y + rem + 1)])
                if total * M - cost >= 0:
                    answer = max(answer, total)
        if answer > 0:
            break
    print(f"#{case} {answer}")
print(time.time() - st)