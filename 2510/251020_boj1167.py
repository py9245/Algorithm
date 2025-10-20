import sys
sys.stdin = open("251020_boj1167.txt", "r")



import sys, heapq

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def uinon(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a


N = int(input())
nodes = []
parent = [i for i in range(N + 1)]
for i in range(1, N + 1):
    nums = list(map(int, input().split()))
    idx = nums[0]
    nums_len = len(nums)
    for i in range(nums_len//2 - 1):
        heapq.heappush(nodes, [-(nums[i * 2 + 2]), idx, nums[i * 2 + 1]])
print(nodes)

