from collections import defaultdict
 
T = int(input())
 
for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int,input().split()))
    max_num = max(nums)
    board = [0] * (max_num + 1)
    ans = 0
    for num in nums:
        for n in range(num + 1):
            board[n] += 1
    for i, v in enumerate(nums):
        ans = max(ans,(N - i) - board[v])
    print(f"#{case} {ans}")