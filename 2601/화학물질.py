import sys

sys.stdin = open("input2.txt", "r")

from collections import deque

T = int(input())

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    cluster = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue

            arr[i][j] = 0
            min_x, min_y, max_x, max_y = i, j, i, j
            queue = deque()
            queue.append((i, j))


            while queue:
                x, y = queue.popleft()

                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                        arr[nx][ny] = 0
                        queue.append((nx, ny))
                        min_x = min(min_x, nx)
                        max_x = max(max_x, nx)
                        min_y = min(min_y, ny)
                        max_y = max(max_y, ny)
            cluster.append([max_x- min_x + 1, max_y - min_y + 1])
    
    print(cluster)

