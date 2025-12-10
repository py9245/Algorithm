import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, M = input().split()
    string = N.replace(M, "a")
    print(f"#{case} {len(string)}")
