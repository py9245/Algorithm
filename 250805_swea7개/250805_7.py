for _ in range(10):
    case = int(input())
    row = [0] * 100
    col = [0] * 100
    x_line = [0, 0]
    for i in range(100):
        for j, v in enumerate(map(int, input().split())):
            row[i] += v
            col[j] += v
            if i == j:
                x_line[0] += v
            elif (99 - i) == j:
                x_line[1] += v
    ans = max(max(row), max(col), max(x_line))
    print(f"#{case} {ans}")