import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dxy = [(0,1),(0,-1),(1,0),(-1,0)]

T = int(input().rstrip())

for case in range(1, T + 1):
    string = deque(input())
    str_len = len(string)
    row = 5
    col = 4 * str_len + 1
    answer_board = [['.'] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if i == 0 or i == 4:
                if j % 4 == 2:
                    answer_board[i][j] = "#"
                else:
                    continue

            elif i == 1 or i == 3:
                if j % 2 == 1:
                    answer_board[i][j] = "#"
                else:
                    continue
            else:
                if not j % 4:
                    answer_board[i][j] = "#"
                elif j % 4 == 2:
                    answer_board[i][j] = string.popleft()
    for line in answer_board:
        print(''.join(line))