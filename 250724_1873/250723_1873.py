T = int(input())

for t in range(1, T + 1):
    H, W = map(int, input().split())
    board = [[] * W for _ in range(H)]
    dirs = ["^", "v", ">", "<"]
    dirS = ["U", "D", "R", "L"]
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cd = 0
    sx, sy = 0, 0
    for i in range(H):
        for j, s in enumerate(input()):
            board[i].append(s)
            if s in dirs:
                sx, sy = i, j
                cd = dirs.index(s)
    cnt = int(input())
    move = input()
    for s in move:
        if s == "S":
            shx, shy = sx, sy
            dx, dy = dir[cd]
            while True:
                nx, ny = shx + dx, shy + dy
                if 0 <= nx < H and 0 <= ny < W:
                    ns = board[nx][ny]
                    if ns == "." or ns == "-" :
                        shx, shy = nx, ny
                    elif ns == "*":
                        board[nx][ny] = "."
                        break
                    else :
                        break
                else :
                    break
        else :
            cd = dirS.index(s)
            dx, dy = dir[cd]
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < H and 0 <= ny < W:
                ns = board[nx][ny]
                if ns == ".":
                    board[nx][ny] = dirs[cd]
                    board[sx][sy] = "."
                    sx, sy = nx, ny
                else :
                    board[sx][sy] = dirs[cd]
            else :
                board[sx][sy] = dirs[cd]
    print(f"#{t}", end = " ")
    for i in board:
        print(''.join(i))