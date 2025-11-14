import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
BASE = 100

for tc in range(1, T + 1):
    # 문자로 입력받음
    str_1 = input()

    # ord로 변환
    str_2 = [ord(i) for i in input()]

    # 변환할 해쉬
    hashing_1 = 0

    # A B C 라면 656667로 변환 파이썬에서는 100글자까지 10 ** 200 으로 표현 가능할 것 같음
    for i, s in enumerate(str_1):
        hashing_1 = hashing_1 * BASE + ord(s)

    # 찾을 숫자의 길이
    check = len(str_1)

    # 해싱한 수 보다 큰 10의 배수 중 가장 작은 수
    # 해싱한 수가 656,667이라면 1,000,000
    # 나머지를 구하기 위해 미리 구해둠
    check_num = int('1' + '0' * len(str(hashing_1)))

    answer = 0


    for i in str_2:
        # 기존 값에 BASE(100)을 곱하고 새로운 문자를 더해줌
        # 기존 문자가 A(65) 였다면 65 * 100 + 다음문자 B(66) = 6566
        answer *= BASE
        answer += i

        # 찾을 숫자의 길이에 도달하기전까지( 0이 되기 전까지) 계속 -= 1 해줌
        if check:
            check -= 1

        # check가 0이라면 아까 구해놓은 check_num로 나눈값만 사용함
        else:
            answer %= check_num

        if answer == hashing_1:
            print(f"#{tc} 1")
            break

    else:
        print(f"#{tc} 0")
