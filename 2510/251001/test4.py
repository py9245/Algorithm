import heapq

arr = [0, 18, 57, 11, 52, 14, 45, 63, 40]

hq = []
for a in arr:
    heapq.heappush(hq, a)
    print(hq)
