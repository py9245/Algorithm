import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    people = [[] for _ in range(N + 1)]
    people[0].append(int(input()))
