import sys
from itertools import combinations as co
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for case in range(1, T + 1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')

    def create_food_score(com):
        score = 0
        for i, j in co(com, 2):
            score += foods[i][j] + foods[j][i]
        return score

    for comb_a in co(range(N), N//2):
        a_food_score = create_food_score(comb_a)
        comb_b = [i for i in range(N) if i not in comb_a]
        b_food_score = create_food_score(comb_b)
        answer = min(abs(a_food_score - b_food_score), answer)
    print(f"#{case} {answer}")