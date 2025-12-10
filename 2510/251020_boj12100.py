import sys
sys.stdin = open("251020_boj12100.txt", "r")

from collections import deque

MAX_CNT = 10
TURN = 4

def gravity_2048(cnt, cbd, col, b_last, last):
    vals = []
    for r in range(N):
        cell = cbd[r][col]
        if cell:
            vals.append(cell[0])

    merged = []
    i = len(vals) - 1
    while i >= 0:
        if i > 0 and vals[i] == vals[i-1]:
            merged.append(vals[i] * 2)
            i -= 2
        else:
            merged.append(vals[i])
            i -= 1

    r = N - 1
    for v in merged:
        cbd[r][col] = [v] + [False] * MAX_CNT
        r -= 1
    while r >= 0:
        cbd[r][col] = 0
        r -= 1

def deep_copy(bd):
    return [[(cell[:] if isinstance(cell, list) else 0) for cell in row] for row in bd]

def rotate90(bd):

    rot = list(zip(*bd[::-1]))
    return [[(cell[:] if isinstance(cell, list) else 0) for cell in row] for row in rot]

def dfs(cnt, bd):
    if cnt > MAX_CNT:
        num = 0
        for i in range(N):
            for j in range(N):
                if bd[i][j]:
                    num = max(num, bd[i][j][0])
        answer[0] = max(answer[0], num)
        return
    
    cur = deep_copy(bd)
    for _ in range(TURN):
        c_bd = deep_copy(cur)
        for c in range(N):
            gravity_2048(cnt, c_bd, c, N - 2, N - 1)
        dfs(cnt + 1, c_bd)
        cur = rotate90(cur)

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            board[i][j] = [board[i][j]] + [False] * 5

answer = [0]
dfs(1, board)
print(answer[0])
