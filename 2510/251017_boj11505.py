import sys

sys.stdin = open("251017_boj11505.txt", "r")

BASE = 10 ** 9 + 7


def init(n, s, e):
    if s == e:
        tree[n] = nums[s]
        return tree[n]

    mid = (s + e) // 2
    tree[n] = (init(n * 2, s, mid) * init(n * 2 + 1, mid + 1, e)) % BASE
    return tree[n]


def update(n, s, e, idx):
    if s > idx or idx > e:
        return tree[n]

    if s == e and s == idx:
        tree[n] = nums[idx]
        return tree[n]

    if s != e:
        mid = (s + e) // 2
        update(n * 2, s, mid, idx)
        update(n * 2 + 1, mid + 1, e, idx)
        tree[n] = tree[n * 2] * tree[n * 2 + 1] % BASE


def find(n, s, e, fs, fe):
    if s > fe or fs > e:
        return 1

    if (s == e) or (fs <= s and e <= fe):
        return tree[n]

    mid = (s + e) // 2
    return (find(n * 2, s, mid, fs, fe) * find(n * 2 + 1, mid + 1, e, fs, fe)) % BASE


N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
tree = [1] * (N * 4)

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        nums[b] = c
        update(1, 0, N - 1, b)
    else:
        print(find(1, 0, N - 1, b, c - 1))
