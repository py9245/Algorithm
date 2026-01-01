import sys

sys.stdin = open("input.txt", "r")

# T = int(input())

# for tc in range(1, T + 1):

from collections import deque

N = int(input())
nums = list(map(int, input().split()))

dp = [1] * N
dp[0] = 1


for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + 1, dp[i])

answer = max(dp)
print(answer)

root = deque()
c_len = answer

for i in range(N - 1, -1, -1):
    if dp[i] == c_len:
        c_len -= 1
        root.appendleft(nums[i])
    if c_len == 0:
        break
print(*root)

