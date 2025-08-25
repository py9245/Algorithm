import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
#
# # N개의 섬 1 ~ N
# # 1섬 구명보트만 다른섬 양 or 늑대
# # 양은 늑대 없는 곳으로 이동
# # 각 섬에서 1번 섬으로 가는 경로 유일
# # i번엔 Pi섬으로 가는 다리 있음
# # 늑대는 움직이지 않고 섬으로 들어온 양들 잡아먹음
# # 늑대 한마리는 최대 한마리만 잡아먹음
# # 최대 얼마나 1번에 도착가능?
#
# # 인풋이 많으니 리드라인 해주고
# # 데이터 정리 어떻게?? 일단 최대 123,456이니 리스트로 공간 만들고 2개 만들고
# # 1에서 아래로? 전체 양 수 더해주고 내려가며 늑대 빼주기?? ㄴㄴ 4노드(늑대)아래 5노드 양이 더 적으면 안댐
# # 공간 3개 만들어주고 정방향 역방향, 늑대는 -N 양은 +N으로 일단 정리
# # 123,456 번 정방향 리스트 순회하며 빈셀부터 찾고 시작 지점으로 갱신
# # 잠깐 한 섬에서 1번 가는 경로 유일이라.. 그러면 위에서 아래로 내려가고 양이면 토탈에 더하다가
# # 늑대면 양 만날때까지 더하고 빼고 하다가 다시 늑대 만날때..... 값 리스트는 공유해도 되겠구나. 그냥 완탐
#
N = int(input())

link = [[] for _ in range(N + 1)]
r_link = [0] * (N + 1)
val_list = [0] * (N + 1)

for i in range(2, N + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    if t == "W":
        a *= -1
    link[p].append(i)
    r_link[i] = p
    val_list[i] = a

indeg = [len(link[i]) for i in range(N+1)]  # 자식 수
q = deque(i for i in range(1,N+1) if indeg[i]==0)  # 리프부터 시작

while q:
    x = q.popleft()
    if x == 1: continue
    p = r_link[x]
    val_list[p] += max(0,val_list[x])
    indeg[p] -= 1
    if indeg[p] == 0:
        q.append(p)
    # 그런대 실패 짜증나서 그냥 부모부터 내려가면서 다 더해주니 성공
    # 이거 탈락 오답으로됨
total = 0
for v in link[1]:
    total += max(0,val_list[v])
print(total)








import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(200000) # 재귀 최대 횟수 늘리기 우리 A형 평가에선 안댐.. 근데 while로도 표현가능
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
animal = [0]*(N+1)   # 양 +, 늑대 -
parent = [0]*(N+1)

for i in range(2, N+1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    if t == "W":
        a = -a
    animal[i] = a
    graph[p].append(i)
    parent[i] = p
#여기까진 동일
def dfs(x):
    total = animal[x]
    for nxt in graph[x]:
        total += dfs(nxt)
    return max(0, total)
#그냥 피보나치처럼 다 더해줬더니 성공했음.. 마이너스든 플러스든 다 더했는데
# 나는 1번 풀이랑 2번풀이랑 뭐가 다른지 잘 모르겠어 풀었는데도
# 이건 합격
print(dfs(1)) #이렇게 하니 성공했음
#어째뜬 이건 쉬운 경우인데 내가 이따가 뭐가 다른지 gpt한테 물어보고 알려줄게
#이런 노드기반 완탐이 있다
# 이런 문제는 부모 -> 자식, 자식 -> 부모 자료형 설정해주고
#이건 특이한 경우로 값까지 같이 관리해서 푼 경우 이런 문제있다 ㅇㅋ
# 다음차례 누구