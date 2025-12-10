T = int(input())

for case in range(1, T + 1):
    N = int(input())
    min_num = 1000000
    max_num = 0
    for num in map(int, input().split()):
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num
    print(f"#{case} {max_num - min_num}")