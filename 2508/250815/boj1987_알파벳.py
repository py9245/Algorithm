import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dxy = [(0,1),(0,-1),(1,0),(-1,0)]

R, C = map(int, input().split())
alpha = [input() for _ in range(R)]
max_len = len({ch for row in alpha for ch in row})

answer = 0
end_point = False

start_mask = 1 << (ord(alpha[0][0]) - ord('A'))
stack = [(0, 0, start_mask, 1)]  # (x, y, visited_mask, total)

while stack:
    x, y, mask, total = stack.pop()

    if total > answer:
        answer = total
        if total == max_len:
            break

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            c_bit = 1 << (ord(alpha[nx][ny]) - ord('A'))
            if not (mask & c_bit):
                stack.append((nx, ny, mask | c_bit, total + 1))

print(answer)
# ---------------------------------------
# import sys
# input = sys.stdin.readline
#
# R,C = map(int,input().split())
# graph = [input().strip() for _ in range(R)]
# max_len = len({ch for row in graph for ch in row})
# dx,dy = [0,0,1,-1],[1,-1,0,0]
#
# def bfs(a,b):
#   q = {(a,b,graph[a][b])}
#   check = [['' for _ in range(C)] for _ in range(R)]
#   check[a][b] = graph[a][b]
#   result = 1
#   while q:
#       x,y,track = q.pop()
#       result = max(result,len(track))
#       if result == max_len:
#         break
#       for i in range(4):
#           nx,ny = x+dx[i],y+dy[i]
#           if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in track and check[nx][ny] != track+graph[nx][ny]:
#             check[nx][ny] = track+graph[nx][ny]
#             q.add((nx,ny,check[nx][ny]))
#   return result
#
# print(bfs(0,0))
