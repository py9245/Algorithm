import sys
sys.stdin = open("251020_boj13460.txt", "r")

from collections import deque

dxy = [(0,1),(1,0),(0,-1),(-1,0)]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

rx = ry = bx = by = ex = ey = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == "B":
            bx, by = i, j
            board[i][j] = '.'
        elif board[i][j] == "O":
            ex, ey = i, j

visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def roll(x, y, dx, dy):
    cnt = 0
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == '#':
            return x, y, cnt, False
        x, y = nx, ny
        cnt += 1
        if (x, y) == (ex, ey):
            return x, y, cnt, True

dq = deque()
dq.append((0, rx, ry, bx, by))
visited[rx][ry][bx][by] = True
bp = False
while dq:
    if bp:
        break
    cnt, crx, cry, cbx, cby = dq.popleft()


    if (cbx, cby) == (ex, ey):
        continue

    if (crx, cry) == (ex, ey):
        bp = True
        print(cnt)
        break

    if cnt >= 10:
        break

    for dx, dy in dxy:
        nrx, nry, rc, r_hole = roll(crx, cry, dx, dy)
        nbx, nby, bc, b_hole = roll(cbx, cby, dx, dy)

        if b_hole:
            continue
        if r_hole:
            print(cnt + 1)
            bp = True
            break

        if (nrx, nry) == (nbx, nby):
            if rc > bc:
                nrx -= dx; nry -= dy
            else:
                nbx -= dx; nby -= dy

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            dq.append((cnt + 1, nrx, nry, nbx, nby))
if not bp:
    print(-1)