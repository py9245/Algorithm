from collections import deque
 
T = int(input())
 
for case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    A, B = A - 1, B - 1
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))
    users = deque((i, t) for i, t in enumerate(map(int,input().split()), start = 1))
 
    wait_N = deque()
    wait_M = deque()
    use_N = [0] * N
    who_N = [[] for _ in range(N)]
    use_M = [0] * M
    who_M = [[] for _ in range(M)]
    use_m_cnt = K
    ans = -1
    t = 0
     
    while use_m_cnt > 0 :
        while users:
            i, c_t = users.popleft()
            if c_t == t :
                wait_N.append(i)
            else:
                users.appendleft((i, c_t))
                break
 
        for i, un in enumerate(who_N):
            if not un and wait_N :
                who_N[i].append(wait_N.popleft())
                use_N[i] = N_arr[i] - 1
            elif use_N[i] > 0:
                use_N[i] -= 1
                 
 
        for i, v in enumerate(use_N): #
            if not v and who_N[i]:
                wait_M.append((who_N[i].pop(),i))
 
        for i, un in enumerate(use_M):
            if not un and wait_M :
                who_M[i].append(wait_M.popleft())
                use_M[i] = M_arr[i] - 1
            elif use_M[i] > 0:
                use_M[i] -= 1
 
         
        for i, v in enumerate(use_M): #
            if not v and who_M[i]:
                use_m_cnt -= 1
                c_num, n_num = who_M[i].pop()
                if n_num == A and i == B:
                    ans = ans + c_num if ans != -1 else c_num
        t += 1
    print(f"#{case} {ans}")