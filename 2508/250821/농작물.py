import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input())) for _ in range(N)]
    rem = N // 2
    ans = 0
    for i in range(N):
        plus = rem - abs(rem - i)
        ans += sum(nums[i][rem - plus: rem + plus + 1])
    print(f"#{case} {ans}")

