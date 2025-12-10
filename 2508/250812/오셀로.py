import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())
dxy = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]

for case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2][N//2], board[N//2 - 1][N//2 - 1] = 2, 2
    board[N // 2][N // 2 - 1], board[N // 2 - 1][N // 2] = 1, 1
    for _ in range(M):
        i, j, color = map(int, input().split())
        i, j = j - 1, i - 1
        board[i][j] = color
        for di, dj in dxy:
            ni, nj = i + di, j + dj
            change = []

            # 보드안에 있고 현재 턴 컬러와 다르면 리스트업
            while 0 <= ni < N and 0 <= nj < N and (3 - board[ni][nj] == color):
                change.append((ni, nj))
                ni, nj = ni + di, nj + dj # 다음 칸 방향에 맞게 업데이트

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == color:# 종료 지점이 보드 안이고 현재 턴 컬러이면 리스트를 변환
                for x, y in change:
                    board[x][y] = color

    black_cnt = sum(c for b in board for c in b if c == 1)# black 구하기
    white_cnt = sum(1 for b in board for c in b if c == 2)# white 구하기

    print(f"#{case} {black_cnt} {white_cnt}")
