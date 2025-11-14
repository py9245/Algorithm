import sys
from collections import defaultdict
sys.stdin = open('input.txt', "r")

T = int(input())

dxy = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
turn = {1: 2, 2: 1, 3: 4, 4: 3}
for case in range(1, T + 1):
    N, M, K = map(int,input().split())
    cell = {}
    for _ in range(K):
        x, y, p, d = map(int,input().split())
        cell[(x, y)] = (p, d)

    for _ in range(M):
        new_cell = defaultdict(list)
        for x, y in cell:
            po, di = cell[(x,y)]
            nx, ny = x + dxy[di][0], y + dxy[di][1]
            if 0 < nx < (N - 1) and 0 < ny < (N - 1):
                new_cell[(nx, ny)].append((po,di))
            else:
                if po == 1:
                    continue
                new_cell[(nx, ny)].append((po//2, turn[di]))
        # print(new_cell)
        cell = {}
        for x, y in new_cell:
            c = new_cell[(x, y)]
            if len(c) == 1:
                cell[(x, y)] = c[0]
            else:
                total = 0
                best_p = 0
                best_d = 0
                for p, d in c:
                    total += p
                    if p > best_p:
                        best_p = p
                        best_d = d
                cell[(x, y)] = (total, best_d)
        # print(cell)

    print(f"#{case} {sum(p for p, d in cell.values())}")


