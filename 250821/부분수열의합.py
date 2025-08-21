import sys
from itertools import combinations as co
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = sorted(map(int, input().split()))
    max_range = 0

    total = 0
    for i in range(N):
        total += nums[i]
        if total > K:
            break
        max_range += 1

    answer = 0

    for i in range(1, max_range + 1):
        for c in co(nums, i):
            num_total = 0
            for num in c:
                num_total += num
                if num_total > K:
                    break
            if num_total == K:
                answer += 1

    print(f"#{case} {answer}")