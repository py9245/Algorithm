import sys
sys.stdin = open("251020_boj1655.txt", "r")

import sys, heapq

input = sys.stdin.readline
N = int(input())

root = int(input())
left = []
l_c = 0
right = []
r_c = 0
answer = [str(root), "\n"]

for i in range(N - 1):
    num = int(input())
    
    if num > root:
        heapq.heappush(right, num)
        r_c += 1
    else:
        heapq.heappush(left, -num)
        l_c += 1

    if l_c > r_c:
        l_c -= 1
        r_c += 1
        heapq.heappush(right, root)
        root = -heapq.heappop(left)
    elif l_c < r_c - 1:
        l_c += 1
        r_c -= 1
        heapq.heappush(left, -root)
        root = heapq.heappop(right)
    # print(f"num : {num}")
    # print(f"root : {root}")
    # print(f"left : {left}")
    # print(f"right : {right}")
    answer.extend([str(root), "\n"])
    # print(answer)
print(''.join(answer[:-1]))



