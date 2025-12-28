import sys

sys.stdin = open("input.txt", "r")

from collections import defaultdict

T = int(input())

dxy = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
HASH = 100

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        new_cell = defaultdict(list)
        for _ in range(len(cell)):
            c = cell.pop()
            n_dir = c[3]
            dx, dy = dxy[n_dir]
            nx, ny = c[0] + dx, c[1] + dy
            #맵 끝 도착
            if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                n_dir += 1
                c[2] = int(c[2] / 2)
                #방향 전환
                if n_dir % 2 != 0:
                    n_dir -= 2
                
            if c[2] > 0:
                new_hash = nx * HASH + ny
                new_cell[new_hash].append([c[2], n_dir])
        # print(new_cell)
        for ncell in new_cell:
            copy_ncell = new_cell[ncell][:]
            x, y = ncell // HASH, ncell % HASH
            
            total_cost = 0
            max_cost = 0
            max_dir = 0
            for nc in copy_ncell:
                cost = nc[0]
                total_cost += cost
            
                if cost > max_cost:
                    max_cost = cost
                    max_dir = nc[1]
                
            cell.append([x, y, total_cost, max_dir])
        # print(f"cell = {cell}")
    print(f"#{tc} {sum(i[2] for i in cell)}")