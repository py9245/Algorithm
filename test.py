import sys

sys.stdin = open("input.txt", "r")

T = int(input())

bdpq = {'b' : 'd', 'd' : "b", "p" : "q", "q" : 'p'}

for case in range(1, T + 1):
    print(f"#{case} {''.join(bdpq[i] for i in input()[::-1])}")