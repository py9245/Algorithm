import sys
sys.stdin = open("input_1.txt", "r")

T = int(input())

dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir = {0: [0, 3, 1, 2, 2, 2, 0, 0, 0, 0, 0],
       1: [1, 2, 3, 3, 0, 3, 1, 1, 1, 1, 1],
       2: [2, 0, 0, 1, 3, 0, 2, 2, 2, 2, 2],
       3: [3, 1, 2, 0, 1, 1, 3, 3, 3, 3, 3]
       }

for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    worm = [[], [], [], [], []]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 5:
                worm[board[i][j] - 6].append((i, j))

    ans = []


    def sol(sx, sy, cx, cy, dr, c):
        nx, ny = cx + dxy[dr][0], cy + dxy[dr][1]

        if not (0 <= nx < N and 0 <= ny < N):
            nd = (dr + 2) % 4

            if (cx, cy, nd) in visited:
                return
            # if visited_dict.get((cx, cy, nd), -1) >= c + 1:
            #     return
            # visited_dict[(cx, cy, nd)] = c + 1
            visited.add((cx, cy, nd))
            sol(sx, sy, cx, cy, nd, c + 1)
            return

        v = board[nx][ny]

        if v == -1 or (nx == sx and ny == sy):
            ans.append(c)
            return

        if v == 0:
            if (nx, ny, dr) in visited:
                return
            # if visited_dict.get((nx, ny, dr), -1) >= c + 1:
            #     return
            # visited_dict[(nx, ny, dr)] = c + 1
            visited.add((nx, ny, dr))
            sol(sx, sy, nx, ny, dr, c)
            return

        if v > 5:
            tx, ty = nx, ny
            for wx, wy in worm[v - 6]:
                if (wx, wy) != (nx, ny):
                    tx, ty = wx, wy
                    break

            if (tx, ty, dr) in visited:
                return
            # if visited_dict.get((tx, ty, dr), -1) >= c + 1:
            #     return
            # visited_dict[(tx, ty, dr)] = c + 1
            visited.add((tx, ty, dr))
            sol(sx, sy, tx, ty, dr, c)
            return

        nd = dir[dr][v]
        if (nx, ny, dr) in visited:
            return
        # if visited_dict.get((nx, ny, dr), -1) >= c + 1:
        #     return
        # visited_dict[(nx, ny, dr)] = c + 1
        visited.add((nx, ny, dr))
        sol(sx, sy, nx, ny, nd, c + 1)


    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            for d in range(4):
                # visited_dict = {}
                visited = set()
                sol(i, j, i, j, d, 0)
    print(f"#{case} {max(ans) if ans else 0}")