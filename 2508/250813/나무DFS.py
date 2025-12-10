import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = max(nums)
    diff = sorted([max_num - n for n in nums if n != max_num])
    diff_len = len(diff)
    ct = diff_len
    cnt = 0

    def dfs():
        global ct
        for i in range(diff_len):
            if diff[i] > 0:
                if water == (1 if diff[i] % 2 else 2):
                    diff[i] -= water
                    if diff[i] == 0:
                        ct -= 1
                    return
        else:
            if water == 2:
                for j in range(diff_len):
                    if diff[j] > 2:
                        diff[j] -= water
                        if diff[i] == 0:
                            ct -= 1
                        return
            elif water == 1:
                for j in range(diff_len):
                    if diff[j] > 1 and ct > 1:
                        diff[j] -= water
                        if diff[i] == 0:
                            ct -= 1
                        return


    while any(diff):
        cnt += 1
        water = 1 if cnt % 2 else 2
        dfs()
    
    print(f"#{case} {cnt}")
