import sys

sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, used, cnt, visi):
    answer[0] = max(answer[0], cnt)

    current = arr[x][y]
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N) or visi[nx][ny]:
            continue
        nxt = arr[nx][ny]
        if nxt < current:
            visi[nx][ny] = True
            dfs(nx, ny, used, cnt + 1, visi)
            visi[nx][ny] = False

        elif not used and nxt - K < current:
            arr[nx][ny] = current - 1
            visi[nx][ny] = True
            dfs(nx, ny, 1, cnt + 1, visi)
            arr[nx][ny] = nxt
            visi[nx][ny] = False


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    start_loc = []
    for i in range(N):
        for j in range(N):
            num = arr[i][j]
            if num > max_num:
                max_num = num
                start_loc = [(i, j)]
            elif num == max_num:
                start_loc.append([i, j])

    answer = [0]    
    # memo = [[[0, 0] for _ in range(N)] for _ in range(N)] #깎은 여부를 나눠 메모

    for x, y in start_loc:
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        dfs(x, y, 0, 1, visited)
        visited[x][y] = False


    # for mem in memo:
    #     for me in mem:
    #         num = max(me)
    #         if answer < num:
    #             answer = num

    print(f"#{tc} {answer[0]}")