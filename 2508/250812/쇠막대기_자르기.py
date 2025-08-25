import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, int(input()) + 1):
    string = input()
    best, stack, posb = 0, 0, True
    for s in string:
        if s == '(':
            stack += 1
            posb = True
        else:
            stack -= 1
            if posb:
                posb = False
                best += stack
            else:
                best += 1
    best += stack
    print(f'#{t} {best}')
