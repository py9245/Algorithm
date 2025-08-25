import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = 10

for case in range(1, T + 1):
    N = int(input())
    ans = 0
    for n in input()[::2]:
        ans += int(n)

    print(f"#{case} {ans}")
