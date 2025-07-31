T = int(input())

for t in range(1,T+1):
    H, W = map(int, input().split())
    board = [[] for _ in range(H)]
    dir = {"^" : -2, "v" : -3, "<" : -4, ">" : -5}
    dir2 = {"U" : -2, "D" : -3, "L" : -4, "R" : -5}
    dir3 = [(0,1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    cd = 0
    sx, sy = 0, 0
    for i in range(H): 
        for j, s in enumerate(input()): #입력 받는 동시에 숫자로 변환
            if s == "<" or s == ">" or s == "^" or s == "v":
                cd = dir[s]
                board[i].append(cd)
                sx, sy = i, j
            elif s == ".":
                board[i].append(0)
            elif s == "*":
                board[i].append(1)
            elif s == "#":
                board[i].append(200)
            elif s == "-":
                board[i].append(-1)
    act = input() #행동 입력
    for a in act:
        if a == "S" : # 슛일경우
            go = True
            sux, suy = sx, sy 
            while True :
                dx, dy = dir3[cd] 
                nx, ny = sux + dx, suy + dy #움직이는 방향쪽
                if 0 <= nx < N and 0 <= ny < N: #배열을 벗어나는지 확인
                    np = board[nx][ny]
                    if np <= 0 :
                        sux, suy = nx, ny
                    else :
                        board[nx][ny] -= 1
                        break
                else :
                    break
        else : # 슟이 아닌 이동인 경우
            cd = dir2[a]
            dx, dy = dir3[cd]
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < N and 0 <= ny < N:
                np = board[nx][ny]
                if np <= 0 :
                    sx, sy = nx, ny
                else :
                    continue
    print(board)
                        
                