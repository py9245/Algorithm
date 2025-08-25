T = int(input())

for case in range(1, T + 1):
    N = int(input())
    min_num, min_idx = 10, 100
    max_num, max_idx = 0, 0
    for i, v in enumerate(map(int, input().split())):
        if v < min_num:
            min_num = v
            min_idx = i
        if v > max_num:
            max_num = v
            max_idx = i
        elif v == max_num:
            max_idx = i
    print(f"#{case} {abs(max_idx - min_idx)}")