from collections import deque
 
T = int(input())
 
dir = [(-1, 0, (2, 5, 6)), (0, 1, (3, 6, 7)), (1, 0, (2, 4, 7)), (0, -1, (3, 4, 5))]
can_dir = {1 : [0, 1, 2, 3], 2 : [0, 2], 3 : [1, 3],
          4 : [0, 1], 5 : [1, 2],
          6 : [2, 3], 7 : [3, 0]
          }
 
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    q.append((R, C, board[R][C], 1))
    board[R][C] = -1
    ans = 1
     
    while q:
        r, c, tun, sec = q.popleft()
        if sec == L:
            continue
        for i in can_dir[tun]:
            dr, dc, can = dir[i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and (board[nr][nc] == 1 or board[nr][nc] in can):
                q.append((nr, nc, board[nr][nc], sec + 1))
                board[nr][nc] = -1 # 0으로 바꿔줘도 괜찮지만 나중 디버깅용으로 -1오
                ans += 1
    print(f"#{t} {ans}")