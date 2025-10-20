import sys

sys.stdin = open("251020_boj13460.txt", "r")

import heapq

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

rx = ry = bx = by = ex = ey = 0

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j
        elif board[i][j] == "O":
            ex, ey = i, j

dist = [[float('inf')] * M for _ in range(N)]
hq = []

heapq.heappush(hq, (0, rx, ry, bx, by, [i[:] for i in board]))

dist[rx][ry] = 0

while hq:
    cnt, crx, cry, cbx, cby, visi = heapq.heappop(hq)
    print(crx, cry)
    if cnt > dist[rx][ry]:
        continue
    
    if cbx == ex and cby == ey:
        continue

    if crx == ex and cry == ey:
        print(cnt)
        break
    
    cnt += 1

    for dx, dy in dxy:
        red_continue = True
        blue_continue = True
        move_rx, move_ry, move_bx, move_by = crx, cry, cbx, cby
        new_visi = [i[:] for i in visi]
        while red_continue or blue_continue:
            if red_continue:
                n_move_rx, n_move_ry = move_rx + dx, move_ry + dy
                if new_visi[n_move_rx][n_move_ry] == "." or new_visi[n_move_rx][n_move_ry] == "O":
                    new_visi[move_rx][move_ry] = "."
                    new_visi[n_move_rx][n_move_ry] = "R"
                    move_rx, move_ry = n_move_rx, n_move_ry
                else:
                    red_continue = False
                if move_rx == ex and move_ry == ey:
                    red_continue = False
            if blue_continue:
                n_move_bx, n_move_by = move_bx + dx, move_by + dy
                if new_visi[n_move_bx][n_move_by] == "." or new_visi[n_move_bx][n_move_by] == "O":
                    new_visi[move_bx][move_by] = "."
                    new_visi[n_move_bx][n_move_by] = "B"
                    move_bx, move_by = n_move_bx, n_move_by
                else:
                    blue_continue = False
                if move_bx == ex and move_by == ey:
                    blue_continue = False
        
        if dist[move_rx][move_ry] > cnt:
            dist[move_rx][move_ry] = cnt
            heapq.heappush(hq, [cnt, move_rx, move_ry, move_bx, move_by, [i[:] for i in new_visi]])
else:
    print(-1)