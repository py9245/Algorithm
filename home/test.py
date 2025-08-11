import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    answer = set()
    turn = N // 4
    string = input()
    for t in range(turn):
        for i in range(4):
            answer.add(int(string[i * turn : (i + 1) * turn], 16))
        string = string[-1] + string[:-1]
    print(f"#{case} {sorted(list(answer))[-K]}")




#부분회문??
    # N = int(input())
    # strings = [input() for _ in range(8)]
    # answer = 0
    # for i in range(8):
    #     for j in range(9 - N):
    #         row = True
    #         col = True
    #         for k in range(N//2):
    #             if not(row and strings[i][j + k] == strings[i][j + (N - k - 1)]):
    #                 row = False
    #             if not(col and strings[j + k][i] == strings[j + (N - k - 1)][i]):
    #                 col = False
    #         if row: answer += 1
    #         if col: answer += 1