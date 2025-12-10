import sys
from collections import defaultdict

sys.stdin = open("../B_type/쏟아지는/input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    candy = sorted(map(int, input().split()))
    answer = candy[-1] - candy[0]
    for i in range(K - 1, N):
        diff = candy[i] - candy[i - K + 1]
        if diff < answer:
            answer = diff
    print(f"#{case} {answer}")