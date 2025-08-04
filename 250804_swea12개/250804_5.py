T = int(input())

for case in range(1, T + 1):
    N = int(input())
    num_list = [0] * 10
    
    for num in input():
        num_list[9 - int(num)] += 1
    max_num = max(num_list)
    print(f"#{case} {9 - num_list.index(max_num)} {max_num}")