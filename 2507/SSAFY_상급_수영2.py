from collections import deque

T = int(input())
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * N for _ in range(N)]
    A, B = map(int, input().split())
    C, D = map(int, input().split()) 

    q = deque()
    q.append((A, B))
    visited[A][B] = 0
    answer = -1
    while q :
        x, y = q.popleft()
        time = visited[x][y]
        if x == C and y == D:
            answer = time
            break
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            cell = board[nx][ny]
            if cell == 1:
                continue
            if cell == 0:
                nt = time + 1
            else:
                if time % 3 == 2:
                    nt = time + 1
                else:
                    wait = (2 - (time % 3)) % 3
                    nt = time + wait + 1
            if visited[nx][ny] == -1 or nt < visited[nx][ny]:
                visited[nx][ny] = nt
                q.append((nx, ny))
    print(f"#{t+1} {answer}")