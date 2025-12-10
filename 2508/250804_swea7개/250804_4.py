T = int(input())

for case in range(1, T + 1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    max_num = 0
    min_num = float('inf')
    for i in range(N - M + 1):
        total = 0
        for j in range(M):
            total += nums[i + j]
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
    print(f"#{case} {max_num - min_num}")