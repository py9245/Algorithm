import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    total = 0
    cnt = 0
    sum_nums = 0
    max_num = 0
    for i in range(N - 1, -1, -1):
        if max_num <= nums[i]:
            if cnt:
                total += max_num * cnt - sum_nums
                cnt = 0
                sum_nums = 0
            max_num = nums[i]
        else:
            cnt += 1
            sum_nums += nums[i]
    print(f"#{case} {total + (max_num * cnt - sum_nums)}")