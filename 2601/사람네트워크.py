import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    node = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
