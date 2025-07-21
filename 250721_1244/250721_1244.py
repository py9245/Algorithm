from itertools import combinations

def sol():
    T = int(input())

    for t in range(1,T+1):
        num, N = input().split()
        num = list(map(int, num))
        N = int(N)
        maxnum = sorted(num, reverse=True)
        answer = set(num)
        answer1 = set()
        comb = set(combinations(N,2))

        if len(set(tuple(num))) == 1: # 조기 종료
            print(f"#{t} {''.join(num)}")

        for _ in range(N): #무조건 N번 바꿔야함
            for nums in answer: #시작은 answer 안에 set으로 num 넣어서 시작
                nums = list(nums)
                for a, b in comb: # N 컴비네이션 2로 경우의 수 set로 반복
                    nums[a], nums[b] = nums[b], nums[a]
                    answer1.add(tuple(nums))
                    nums[a], nums[b] = nums[b], nums[a]
                answer = answer1
        print(f"#{t} {max([int(''.join(n)) for n in answer])}")