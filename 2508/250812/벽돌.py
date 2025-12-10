import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


for case in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(H)]
    new_board = [list(v) for v in zip(*board[::-1])]
    best = [0]
    initial = sum(1 for x in range(W) for y in range(H) if new_board[x][y] > 0)

    def explode(bd, x, y): # 연쇄 폭발
        if bd[x][y] == 0:
            return 0
        q = deque()
        q.append((x, y, bd[x][y]))
        bom = 0
        bd[x][y] = 0
        bom += 1

        while q:
            cx, cy, power = q.popleft()
            if power <= 1:
                continue
            for dx, dy in dxy:
                nx, ny = cx, cy
                for _ in range(1, power):
                    nx += dx
                    ny += dy
                    if not (0 <= nx < W and 0 <= ny < H):
                        break
                    if bd[nx][ny] == 0:
                        continue
                    nxt_p = bd[nx][ny] # nxny 칸 파워
                    bd[nx][ny] = 0
                    bom += 1
                    if nxt_p > 1:
                        q.append((nx, ny, nxt_p))
        return bom


    def gravity(bd):
        for x in range(W):
            stack = [bd[x][y] for y in range(H) if bd[x][y] != 0]

            for y in range(H):# 전부 비움
                bd[x][y] = 0

            for y, val in enumerate(stack):# 아래부터 채우기
                bd[x][y] = val

    def boom(n, bd, total):
        # n == 0 basis 조건
        if n == 0:
            if total > best[0]:
                best[0] = total
            return

        for i in range(W):
            j_hit = None
            for y in range(H - 1, -1, -1):
                if bd[i][y] > 0:
                    j_hit = y
                    break
            if j_hit is None:
                continue

            nxt = [col[:] for col in bd]
            gained = explode(nxt, i, j_hit)
            gravity(nxt)
            boom(n - 1, nxt, total + gained)

        # best 갱신 진행중인 재귀 없애기
        if all(bd[x][y] == 0 for x in range(W) for y in range(H)):
            if total > best[0]:
                best[0] = total

    boom(N, [col[:] for col in new_board], 0)
    print(f"#{case} {initial - best[0]}")