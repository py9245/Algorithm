import sys

sys.stdin = open('input.txt', "r")

from collections import deque

T = int(input())

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

for case in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    answer_board = [[0] * N for _ in range(N)]

    check_list = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] == "*": # 지뢰가 있는곳
                answer_board[i][j] = 10 # answer_board에 그냥 10으로 정의
                for di, dj in dxy: # answer_board에 지뢰는 10으로 지뢰의 8방면은 1씩 더해줌
                    ni, nj = i + di, j + dj
                    if not(0 <= ni < N and 0 <= nj < N) or board[ni][nj] == "*":
                        continue
                    answer_board[ni][nj] = 1
                    check_list.add((ni, nj))

    answer = len(check_list)

    for i in range(N):
        for j in range(N):
            if answer_board[i][j] == 0:
                answer_board[i][j] = 10
                answer += 1
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.pop()

                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if not(0 <= nx < N and 0 <= ny < N):
                            continue
                        num = answer_board[nx][ny]
                        answer_board[nx][ny] = 10
                        if not num:
                            q.append((nx, ny))

                        elif num == 1:
                            answer -= 1

    print(f"#{case} {answer}")