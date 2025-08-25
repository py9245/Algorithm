import sys
from collections import deque
sys.stdin = open("input.txt", "r")

#T = int(input())

for case in range(1, 11):
    input()
    nums = deque(map(int, input().split()))
    num = 1
    while num:
        for i in range(1, 6):
            num = nums.popleft()
            num = max(num - i, 0)
            nums.append(num)
            if not num:
                break
    answer = ' '.join(map(str,nums))

    print(f"#{case} {answer}")

    # import sys
    from collections import defaultdict

    # sys.stdin = open("input.txt", "r")
    #
    # T = int(input())
    #
    # for case in range(1, T + 1):
    #     N, K = map(int, input().split())
    #     check = '1' * K
    #     board = [''.join(input().split()) for _ in range(N)]
    #     row_l = sum(1 for i in board for j in i.split('0') if j == check)
    #     col_l = sum(1 for i in zip(*board) for j in ''.join(i).split('0') if j == check)
    #     print(f"#{case} {row_l + col_l}")
