import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, T = map(int, input().split())

y_x_idx = [{} for _ in range(T + 1)]

for _ in range(N):
    x, y = map(int, input().split())
    y_x_idx[y][x] = True

q = deque()
q.append((0, 0, 0, set())) # y, x, cnt

best = N + 1

memo = {}

while q:
    y, x, cnt, visi = q.popleft()

    if cnt >= best:
        continue

    if memo.get((y, x), N + 1) <= cnt or (y, x) in visi:
        continue

    if y == T:
        best = cnt
        continue

    visi.add((y, x))
    memo[(y, x)] = cnt

    for dy in range(2, -3, -1):
        for dx in range(2, -3, -1):
            if dx == 0 and dy == 0: # 0,0 본인은 할 필요 없음
                continue
            ny, nx = y + dy, x + dx

            if not(0 <= ny < (T + 1) and 0 <= nx): #좌표 아래로 내려가면 false
                continue

            if y_x_idx[ny].get(nx, 0):
                q.append((ny, nx, cnt + 1, visi))

print(-1 if best == N + 1 else best)