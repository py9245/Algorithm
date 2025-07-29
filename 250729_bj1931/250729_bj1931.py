import sys
input = sys.stdin.readline

N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
rooms.sort(key=lambda x: (x[1], x[0])) #의미는 rooms안의 리스트의 1인덱스 값을 우선으로 오름차순, 0인덱스 기준 오름차순 정렬

end = -1
cnt = 0

for s, e in rooms :
    if s >= end:
        cnt += 1
        end = e
print(cnt)