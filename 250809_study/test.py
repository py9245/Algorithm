# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    people = []
    outers = []
    for i in range(N):
        for j in range(N):
            num = board[i][j]
            if num > 1:
               outers.append([i,j,num])
            elif num == 1 :
               people.append([i, j]) 
    dist_people = []
    for x, y in people:
        dists = []
        for dx, dy, v in outers:
            dists.append((abs(x - dx) + abs(y - dy)))
        dists.append(dists)
    print(dist_people)