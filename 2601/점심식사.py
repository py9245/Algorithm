import sys

# sys.stdin = open("input.txt", "r")

def simulate(arrival_times, stair_cost):
    """
    특정 계단에 배정된 사람들의 도착 시간 리스트를 받아 
    해당 계단의 모든 사람이 탈출하는 최소 시간을 계산합니다.
    """
    if not arrival_times:
        return 0
    
    arrival_times.sort() # 먼저 도착한 순서대로 정렬
    stair_queue = []     # 현재 계단을 내려가는 중인 사람들의 [완료 예정 시간]
    time = 0
    
    # 마지막 사람이 계단을 다 내려올 때까지 반복
    while arrival_times or stair_queue:
        time += 1
        
        # 1. 계단을 다 내려온 사람 제거
        while stair_queue and stair_queue[0] <= time:
            stair_queue.pop(0)
            
        # 2. 계단 진입 시도 (최대 3명)
        # arrival_times[0]은 도착 시간(+1 포함)이므로 time과 비교 가능
        while arrival_times and arrival_times[0] <= time:
            if len(stair_queue) < 3:
                # 계단 진입: 현재 시간 + 계단 길이
                stair_queue.append(time + stair_cost)
                arrival_times.pop(0)
            else:
                # 계단이 꽉 찼으면 다음 초에 다시 시도
                break
                
    return time

# 입력 처리

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    stairs = []  # (r, c, cost)
    peoples = [] # (r, c)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                peoples.append((i, j))
            elif arr[i][j] > 1:
                stairs.append((i, j, arr[i][j]))
    
    num_p = len(peoples)
    first_step_cost = stairs[0][2]
    second_step_cost = stairs[1][2]

    # 각 사람의 계단별 도착 시간 미리 계산 (도착 1분 후 진입 조건 포함)
    p_dists = []
    for p in peoples:
        d1 = abs(p[0] - stairs[0][0]) + abs(p[1] - stairs[0][1]) + 1
        d2 = abs(p[0] - stairs[1][0]) + abs(p[1] - stairs[1][1]) + 1
        p_dists.append((d1, d2))

    min_total_time = float('inf')

    # 비트마스크 탐색: 2^num_p 가지 경우의 수
    # i의 j번째 비트가 0이면 1번 계단, 1이면 2번 계단 선택
    for i in range(1 << num_p):
        group1 = []
        group2 = []
        
        for j in range(num_p):
            if i & (1 << j):
                group2.append(p_dists[j][1])
            else:
                group1.append(p_dists[j][0])
        
        # 각 계단 시뮬레이션 결과 중 더 큰 값이 해당 경우의 전체 소요 시간
        res1 = simulate(group1, first_step_cost)
        res2 = simulate(group2, second_step_cost)
        
        current_max = max(res1, res2)
        if current_max < min_total_time:
            min_total_time = current_max

    print(f"#{tc} {min_total_time}")
