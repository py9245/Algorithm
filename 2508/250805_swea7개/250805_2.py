from collections import deque

T = int(input())

for case in range(1, T + 1): # zzz
    find_string = deque(input())
    ALL_string = deque(input())
    find_s_len = len(find_string)
    cnt = 0
    q = deque()
    while ALL_string:
        string = ALL_string.popleft()
        q.append(string)
        cnt += 1
        if cnt > find_s_len:
            q.popleft()
            cnt -= 1
        if q == find_string:
            print(f"#{case} 1")
            break
    else :
        print(f"#{case} 0")