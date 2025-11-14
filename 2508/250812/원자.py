import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for case in range(1, T + 1):
    N = int(input())
    cell_dir = defaultdict(list)
    best = 0
    for i in range(N):
        x, y, d, p = map(int, input().split())
        cell_dir[(x*2, y*2)].append((d, p))

    
    while cell_dir:
        new_cell_dir = defaultdict(list)
        for x, y in cell_dir:
            d,  p = cell_dir[(x, y)][0]
            nx, ny = x + dxy[d][0], y + dxy[d][1]
            if not(-2000<= nx <= 2000 and -2000<= ny <= 2000):
                continue
            new_cell_dir[(nx, ny)].append((d, p))
        for key in list(new_cell_dir):
            if len(new_cell_dir[key]) > 1:
                pop_cell = new_cell_dir.pop(key)
                for d, p in pop_cell:
                    best += p
        cell_dir = new_cell_dir
    print(f"#{case} {best}")
