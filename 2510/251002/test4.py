import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    d, m, tm, y = map(int, input().split())
    dp = [d * 30, m, tm, y]
    for i in range(12)


    print(f"#{tc} {max(dp.values())}")