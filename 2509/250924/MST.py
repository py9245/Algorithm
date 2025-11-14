import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
#
# import heapq
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N, M = map(int, input().split())
#     line = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         p, c, d = map(int, input().split())
#         heapq.heappush(line[p], [d, c])
#         heapq.heappush(line[c], [d, p])
#
#     hq = []
#     visi = set()
#     answer = 0
#     end_point = 0
#     for i, n in enumerate(line):
#         if n:
#             visi.add(i)
#             ene_point = i
#             for nd, nc in n:
#                 heapq.heappush(hq, [nd, i, nc])
#             break
#
#     while hq:
#         d, s, e = heapq.heappop(hq)
#
#         if e in visi:
#             continue
#         visi.add(e)
#         answer += d
#         for nd, ne in line[e]:
#             if ne in visi:
#                 continue
#             heapq.heappush(hq, [nd, e, ne])
#     print(f"#{case} {answer}")

def find_set(x):
    global p_list
    if p_list[x] != x:
        p_list[x] = find_set(p_list[x])
    return p_list[x]


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    p_list = list(range(V + 1))
    cnt = 0
    answer = 0
    rank = [0] * (V + 1)
    nums = [list(map(int, input().split())) for _ in range(E)]
    nums.sort(key=lambda x: x[2])
    for i in range(E):
        n1, n2, w = nums[i]
        x = find_set(n1)
        y = find_set(n2)

        if x != y:
            answer += w
            cnt += 1
            if rank[x] > rank[y]:
                p_list[y] = x
            elif rank[x] < rank[y]:
                p_list[x] = y
            else:
                p_list[y] = x
                rank[x] += 1
        if cnt == V:
            break

    print(f'#{t} {answer}')