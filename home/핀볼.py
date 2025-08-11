import sys
sys.stdin = open('input.txt', 'r')

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

bounce_dict = {
        1 : [1, 3, 0, 2],
        2 : [3, 0, 1, 2],
        3 : [2, 0, 3, 1],
        4 : [1, 2, 3, 0],
        5 : [1, 0, 3, 2]
    }

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    worm = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            v = board[i][j] - 6
            if 0 <= v <= 4:
                worm[v].append((i, j))

    worm_dict = {}

    for i in range(5):
        if worm[i]:
            worm_dict[worm[i][0]] = worm[i][1]
            worm_dict[worm[i][1]] = worm[i][0]

    
 
    def pin_ball(i, j, dir):
 
        si, sj, dir = i, j, dir
        score = 0 
         
        while True:
            ni, nj = i + dxy[dir][0], j + dxy[dir][1]
             
            # 벽에 부딪힌 경우
            if not (0 <= ni < N and 0 <= nj < N) or board[ni][nj] == 5:
                i, j = ni, nj
                dir = bounce_dict[5][dir]
                score += 1
                continue
             
            if (ni, nj) == (si, sj) or board[ni][nj] == -1:
                return score
             
            # 물체에 부딪힌 경우
            if 1 <= board[ni][nj] <= 4:
                dir = bounce_dict[board[ni][nj]][dir]
                score += 1
                i, j = ni, nj
                continue
             
            # 웜홀에 빠진 경우
            if 6 <= board[ni][nj] <= 10:
                ni, nj = worm_dict[(ni, nj)]
                i, j = ni, nj
                continue
             
            i, j = ni, nj
    
    max_score = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in [0, 1, 2, 3]:
                    max_score = max(max_score, pin_ball(i, j, d))
 
    print(f'#{case} {max_score}')