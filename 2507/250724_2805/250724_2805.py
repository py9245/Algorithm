T = int(input())

for t in range(1, T + 1):
    N = int(input())
    re = N // 2
    add_num = -1
    answer = 0
    for i in range(N):
        nums = list(map(int,input()))
        if i <= re:
            add_num += 1
        else :
            add_num -= 1
        answer += sum(nums[re - add_num : re + add_num + 1])
    print(f"#{t} {answer}")
            