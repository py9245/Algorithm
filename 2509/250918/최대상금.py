import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')

def sol():
    T = int(input())

    for t in range(1, T+1):
        num, N = input().split()
        num = list(num)  # 문자열 그대로 리스트로
        N = int(N)
        answer = {tuple(num)}  # 시작값을 집합에 저장
        comb = set(combinations(range(len(num)), 2))  # 자리 교환 조합

        if len(set(num)) == 1:  # 모든 숫자가 같으면 조기 종료
            print(f"#{t} {''.join(num)}")
            continue

        for _ in range(N):  # N번 교환
            answer1 = set()
            for nums in answer:
                numss = list(nums)
                for a, b in comb:
                    numss[a], numss[b] = numss[b], numss[a]
                    answer1.add(tuple(numss))
                    numss[a], numss[b] = numss[b], numss[a]  # 원복
            answer = answer1

        print(f"#{t} {max(int(''.join(n)) for n in answer)}")
sol()
