import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
STAN = 10544
DAD = 44324

for case in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell_dict = defaultdict(list)

    for _ in range(K):
        i, j, p, d = map(int, input().split())
        key = i * STAN + j + DAD
        cell_dict[key] = [p, d - 1]

    for h in range(M):
        new_cell_dict = defaultdict(list)
        for k in cell_dict:
            p, d = cell_dict[k]
            x, y = divmod((k - DAD), STAN)
            nx, ny = x + dxy[d][0], y + dxy[d][1]
            new_k = nx * STAN + ny + DAD
            if not(0 < nx < N - 1 and 0 < ny < N - 1):
                if d % 2 == 0:
                    d += 1
                else:
                    d -= 1
                new_cell_dict[new_k].append((int(p//2), d))
            else:
                new_cell_dict[new_k].append((p, d))

        for k in list(new_cell_dict):
            value = new_cell_dict[k]
            nd = 0
            max_p = 0
            sum_p = 0
            for p, d in value:
                sum_p += p
                if max_p < p:
                    max_p = p
                    nd = d
            new_cell_dict[k] = [sum_p, nd]

        cell_dict = new_cell_dict

    answer = 0
    for p, d in cell_dict.values():
        answer += p

    print(f"#{case} {answer}")