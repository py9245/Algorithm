import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, 11):
    input()
    nums = list(map(int, input().split()))
    min_num = min(nums) - 1
    for i in range(16):
        if i // 8 > 0:
            num = muns.popleft() - 1
            if num == 0:
                nums.append(num)

    while True:


    print(f"#{case} {nums[M % N]}")