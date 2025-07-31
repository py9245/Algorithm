# T = int(input())

# for t in range(1, T + 1):
#     N = int(input()) # 수영장 크기 N * N 크기로
#     board = [list(map(int, input().split())) for _ in range(N)] #수영장 모양
#     visited = [[False] * N for _ in range(N)]
#     A, B = map(int, input().split()) #시작하는 위치
#     C, D = list(map(int, input().split())) #도착지점 위치 
#     dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른, 아래, 왼, 위 방향
#     answer = []

#     def dfs(x, y, s):
#         visited[x][y] = True
#         if x == C and y == D:
#             answer.append(s)
#         for dx, dy in dir:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N :
#                 if board[nx][ny] == 1 or visited[nx][ny]:
#                     continue
#                 elif not visited[nx][ny]:
#                     if board[nx][ny] == 0:
#                         bfs(nx, ny, s + 1)
#                     elif board[nx][ny] == 2:
#                         bfs(nx, ny, s + (3 - s % 3))
                
#     bfs(A, B, 0)
#     print(f"#{t} {min(answer)}")
dfs 아님ㅠㅠㅠㅠㅠㅠ
        