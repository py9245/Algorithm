T = int(input())

for t in range(1, T + 1):
    N = int(input()) # 수영장 크기 N * N 크기로
    board = [list(map(int, input().split())) for _ in range(N)] #수영장 모양
    visited = [[False] * N for _ in range(N)]
    A, B = map(int, input().split()) #시작하는 위치
    C, D = map(int, input().split()) #도착지점 위치 
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른, 아래, 왼, 위 방향
    answer = float("inf")


