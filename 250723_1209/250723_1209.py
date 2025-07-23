for _ in range(1, 11):
    t = int(input())
    row = [0 for _ in range(100)]
    col = [0 for _ in range(100)]
    bsl = 0
    sl = 0
    for i in range(100):
        for j, n in enumerate(map(int, input().split())):
            row[i] += n
            col[j] += n
            if i == j :
                bsl += n
            if i + j == 99:
                sl += n
    print(f"#{t} {max(max(col),max(row),bsl,sl)}")cd