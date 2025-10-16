import sys

sys.stdin = open("251016_boj2042.txt", "r")

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
seg_tree = [0] * (N * 4)


def build(n, s, e):
    if s == e:
        seg_tree[n] = nums[s]
        return seg_tree[n]

    mid = (s + e) // 2
    left = build(n * 2, s, mid)
    right = build(n * 2 + 1, mid + 1, e)
    seg_tree[n] = left + right
    return seg_tree[n]


def chang(n, s, e, fn, val):
    if fn < s or fn > e:
        return
    seg_tree[n] += val
    if s != e:
        mid = (s + e) // 2
        chang(n * 2, s, mid, fn, val)
        chang(n * 2 + 1, mid + 1, e, fn, val)


def find(n, s, e, fs, fe):
    if fe < s or e < fs:  # 완전히 벗어남
        return 0
    if fs <= s and e <= fe:  # 완전히 포함됨
        return seg_tree[n]
    mid = (s + e) // 2

    return find(n * 2, s, mid, fs, fe) + find(n * 2 + 1, mid + 1, e, fs, fe)


build(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b - 1
        chang(1, 0, N - 1, idx, c - nums[idx])
        nums[idx] = c
    else:
        s, e = b - 1, c - 1
        print(find(1, 0, N - 1, s, e))
#
#
#
#         M + K

from collections import defaultdict

result_list = []
N, M, K = map(int, input().split())
N_dict = {}

# 여러 버킷 크기 설정 (필요할수록 확장)
bucket_sizes = [1, 2, 3, 4, 5, 10, 25, 50, 100, 250, 500, 1000, 2000, 3000, 100000]
bucket_dicts = {b: defaultdict(int) for b in bucket_sizes}

# 데이터 입력 및 버킷별 누적합 초기화
for i in range(1, N + 1):
    N_dict[i] = int(input().strip())
    for b in bucket_sizes:
        bucket_dicts[b][i // b] += N_dict[i]

# 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:  # 값 갱신
        diff = c - N_dict[b]
        N_dict[b] = c
        for size in bucket_sizes:
            bucket_dicts[size][b // size] += diff

    else:  # 구간합 계산
        result = 0
        cnt = c - b + 1
        temp = b

        while cnt > 0:
            # 가장 큰 버킷부터 탐색
            for size in reversed(bucket_sizes):
                if temp % size == 0 and cnt >= size:
                    result += bucket_dicts[size][temp // size]
                    cnt -= size
                    temp += size
                    break
            else:
                result += N_dict[temp]
                cnt -= 1
                temp += 1

        result_list.append(f"{result}\n")

print(''.join(result_list))
