import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    num = float(input())
    answer = ''
    for i in range(-1, -13, -1):
        new_num = num - 2 ** i
        if new_num < 0:
            answer += '0'
        else:
            answer += '1'
            num = new_num

        if new_num == 0.0:
            print(f"#{case} {answer}")
            break
    else:
        print(f"#{case} overflow")