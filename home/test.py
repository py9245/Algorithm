import sys
sys.stdin = open('input.txt', 'r')

dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

dir_next = {
    0: [0, 3, 1, 2, 2, 2, 0, 0, 0, 0, 0],
    1: [1, 2, 3, 3, 0, 3, 1, 1, 1, 1, 1],
    2: [2, 0, 0, 1, 3, 0, 2, 2, 2, 2, 2],
    3: [3, 1, 2, 0, 1, 1, 3, 3, 3, 3, 3],
}

T = int(input())
for case in range(1, T + 1):
    N = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(N)]
    worm = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            v = board[i][j] - 6
            if 0 <= v <= 4:
                worm[v].append((i, j))

    worm_dict = {}
    for i in range(5):
        if worm[i]:
            worm_dict[worm[i][0]] = worm[i][1]
            worm_dict[worm[i][1]] = worm[i][0]
    
    best = 0
    visited_dict = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            for d in range(4):
                if (i == 0 and d == 3) or (i == N - 1 and d == 1):
                    best = max(1, best)
                    continue
                if (j == 0 and d == 0) or (j == N - 1 and d == 2):
                    best = max(1, best)
                    continue
                x, y = i, j
                total = 0
                while True:
                    nx, ny = x + dxy[d][0], y + dxy[d][1]

                    if not (0 <= nx < N and 0 <= ny < N):
                        d = dir_next[d][5]
                        total += 1
                        if visited_dict.get((x, y, d), -1) >= total:
                            break
                        visited_dict[(x, y, d)] = total
                        x += dxy[d][0]
                        y += dxy[d][1]
                        if (x, y) == (i, j):
                            best = max(best, total)
                            break
                        continue   

                    v = board[nx][ny]

                    if v == -1 or (nx == i and ny == j):
                        best = max(total, best)
                        break

                    if v == 0:
                        x, y = nx, ny
                        if visited_dict.get((x, y, d), -1) >= total:
                            break
                        visited_dict[(x, y, d)] = total
                        continue

                    if v > 5:
                        tx, ty = worm_dict[(nx, ny)]
                        x, y = tx, ty
                        if visited_dict.get((x, y, d), -1) >= total:
                            break
                        visited_dict[(x, y, d)] = total
                        continue

                    nd = dir_next[d][v]
                    x, y, d = nx, ny, nd
                    total += 1
                    if visited_dict.get((x, y, d), -1) >= total:
                        break
                    visited_dict[(x, y, d)] = total
    print(f"#{case} {best}")