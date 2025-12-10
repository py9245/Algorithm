T = int(input())

for case in range(1, T + 1):
    case, N = input().split()
    num_string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dict = {num_string[i] : i for i in range(10)}
    num_dict_reverse = {i : num_string[i] for i in range(10)}
    print_arr = [num_dict_reverse[num] for num in sorted(num_dict[s] for s in input().split())]
    print(case)
    print(*print_arr)