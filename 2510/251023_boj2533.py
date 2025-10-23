import sys
sys.stdin = open("251023_boj2533.txt", "r")

from collections import defaultdict
import heapq

N = int(input())

friends = [[] for _ in range(N + 1)]

counter = defaultdict(int)

for _ in range(N - 1):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
    counter[a] += 1
    counter[b] += 1

hq = []
answer = 0
visi = set()

start_idx = 0
start_val = 0

for i in range(N + 1):
    if start_val < counter[i]:
        start_idx = i
        start_val = counter[i]

heapq.heappush(hq, [-start_val, start_idx])
break_cnt = N - 2

while hq:
    cnt, idx = heapq.heappop(hq)
    print(cnt, idx)
    if idx in visi:
        continue

    visi.add(idx)
    answer += 1
        
    if break_cnt == 0:
        break

    for n_idx in friends[idx]:
        if n_idx in visi:
            continue
        break_cnt += 1
        heapq.heappush(hq, [-counter[n_idx], n_idx])
print(answer)
    
