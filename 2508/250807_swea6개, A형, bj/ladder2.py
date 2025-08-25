dj = [1, -1, 1]

for _ in range(10):
    case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    best = (0,float('inf'))
    for j in range(100):
        if not board[0][j]:
            continue
        cnt = -1
        dir = 0
        x, y = 0, j
        while x < 99:
            cnt += 1
            if dir == 0:
                if y - 1 >= 0 and board[x][y - 1] == 1:
                    dir = 1
                    y -= 1
                elif y + 1 < 100 and board[x][y + 1] == 1:
                    dir = 2
                    y += 1
                else :
                    x += 1
            else :
                if not board[x+1][y]:
                    y += dj[dir]
                else :
                    dir = 0
                    x += 1
        if best[1] >= cnt:
            best = (j, cnt)
    print(f"#{case} {best[0]}")