import sys
sys.stdin = open("251020_boj1655.txt", "r")

minv, maxv = map(int, input().split())
is_sqfree = [True] * (maxv - minv + 1)

i = 2
while i * i <= maxv:
    sq = i * i
    # minv 이상인 첫 배수를 찾아야 함
    start = ((minv + sq - 1) // sq) * sq
    
    for x in range(start, maxv + 1, sq):
        is_sqfree[x - minv] = False
    i += 1

print(sum(is_sqfree))
