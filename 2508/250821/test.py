import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    arr.sort()
    best = [0]
    dp = defaultdict(lambda: float('INF'))
    dp[arr[0][1]] = arr[0][0]
    for c_w, c_v in arr:
        for key_val in list(dp): # dp의 키를 가치로 둠
            new_w = dp[key_val] + c_w # 여태까지 key_val의 가치를 가지는 것 중 가장 작은 무게 + 현재 무게
            new_v = key_val + c_v
            if new_w <= K and dp[new_v] > new_w:
                dp[new_v] = new_w
        if dp[c_v] > c_w:
            dp[c_v] = c_w
    print(dp)