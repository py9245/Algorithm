N = int(input())

ans = list(map(int, input().split())) #이게 만족해야 정답임
visited = [False] * N #방문확인
men = []

def sol():
    if len(men) == N : # 종료조건인데 men이 여태까지 조건에 맞춰 전부 append 됐으면 자동 정답
        answer = [i + 1 for i in men]
        print(*answer)
        exit()
    for i in range(N):
        if visited[i]:
            continue
        if ans[i] == sum(x > i for x in men):
            men.append(i)
            visited[i] = True
            sol()
            men.pop()
            visited[i] = False
sol()