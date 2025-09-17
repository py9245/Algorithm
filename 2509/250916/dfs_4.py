import sys
from collections import deque
sys.stdin = open('input.txt', "r")

T = int(input())
N = 4



for _ in range(T):
    case = int(input())
    chain = [list(map(int, input().split())) for _ in range(1, T + 1)]

    print(f"#{case} {answer}")

