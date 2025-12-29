import sys

sys.stdin = open("input.txt", "r")

def operate(op_type, num1, num2):
    if op_type == 0: return num1 + num2
    if op_type == 1: return num1 - num2
    if op_type == 2: return num1 * num2
    if op_type == 3: return int(num1 / num2)

for t in range(1, int(input()) + 1):
    N = int(input())
    init_opers = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    dp = [set() for _ in range(N)]
    dp[0].add((nums[0], init_opers))
    
    for idx in range(1, N):
        next_num = nums[idx]
        for current_val, opers in dp[idx-1]:
            for i in range(4):
                if opers[i] > 0:
                    
                    res = operate(i, current_val, next_num)
                    new_op_list = list(opers)
                    new_op_list[i] -= 1
                    
                    dp[idx].add((res, tuple(new_op_list)))

    results = [d[0] for d in dp[N-1]]
    print(f"#{t} {max(results) - min(results)}")