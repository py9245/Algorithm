import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(N)]

    def find_line():
        for i in range(N):
            row = 0
            col = 0
            for j in range(N):
                if matrix[i][j] == "o":
                    row += 1
                else:
                    row = 0

                if matrix[j][i] == "o":
                    col += 1
                else:
                    col = 0

                if row == 5 or col == 5:
                    print(f"#{case} YES")
                    return False
        return True
                
    def find_diagonal():
        diago = []
        reverde_diago = []

        for s in range(2 * N - 1):
            dia = 0
            r_dia = 0
            for i in range(N):
                j = s - i
                if 0 <= j < N:
                    if matrix[i][j] == 'o':
                        dia += 1
                    else:
                        dia = 0

                    if matrix[i][N - 1 - j] == 'o':
                        r_dia += 1
                    else:
                        r_dia = 0
                if dia == 5 or r_dia == 5:
                    print(f"#{case} YES")
                    return False
        return True
    
    if find_line() and find_diagonal():
        print(f"#{case} NO")


