from collections import deque, defaultdict
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

for case in range(1, T + 1):
    M, A = map(int, input().split())
    A_map = [0] + list(map(int, input().split()))
    B_map = [0] + list(map(int, input().split()))
    charge_dict = defaultdict(list)

    for ap in range(A):
        x, y, r, p = map(int, input().split())
        for dx in range(-r, r + 1):
            rem = r - abs(dx)
            for dy in range(-rem, rem + 1):
                nx, ny = x + dx, y + dy
                if 1 <= nx <= 10 and 1 <= ny <= 10:
                    charge_dict[(nx, ny)].append((p, ap))
                    
    for key in charge_dict:
        charge_dict[key].sort(reverse=True)
        
    print(charge_dict)
    Ax, Ay, Bx, By = 1, 1, 10, 10
    total = 0
    
    for idx in range(M + 1):
        ad, bd = A_map[idx], B_map[idx]
        Ax, Ay = Ax + dxy[ad][0], Ay + dxy[ad][1]
        Bx, By = Bx + dxy[bd][0], By + dxy[bd][1]
        
        A_arr = charge_dict[(Ax, Ay)]
        B_arr = charge_dict[(Bx, By)]
        
        if not A_arr and not B_arr:
            pass
        elif not A_arr:
            total += B_arr[0][0]
        elif not B_arr:
            total += A_arr[0][0] 
        else:
            
            Ap, Aid = A_arr[0]
            Bp, Bid = B_arr[0]
            if Aid != Bid:
                total += Ap + Bp
            else:
                a2 = A_arr[1][0] if len(A_arr) > 1 else 0
                b2 = B_arr[1][0] if len(B_arr) > 1 else 0
                # 둘 중 한 명이 다른 AP로 갈 때의 이득을 더해 최대화
                total += Ap + max(a2, b2)
    print(total)