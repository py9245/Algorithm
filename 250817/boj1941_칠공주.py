import sys

sys.stdin = open("input.txt", "r")

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
N = 5

student = []

for _ in range(N):
    add_list = []
    for s in input().strip():
        if s == "Y":
            add_list.append(1)
        else:
            add_list.append(0)
    student.append(add_list)
answer = set()

def dfs(total, y_cont, idx_hash, cells):
    if total == 7:
        answer.add(idx_hash)
        return

    tried = set()
    for (x, y) in cells:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                next_hash = 1 << (nx * 5 + ny)
                if next_hash in tried:
                    continue
                tried.add(next_hash)
                if not (idx_hash & next_hash) and y_cont + student[nx][ny] < 4:
                    cells.append((nx, ny))
                    dfs(total + 1, y_cont + student[nx][ny], idx_hash | next_hash, cells)
                    cells.pop()

for i in range(N):
    for j in range(N):
        dfs(1, student[i][j], 1 << (i * 5 + j), [(i, j)])

print(len(answer))