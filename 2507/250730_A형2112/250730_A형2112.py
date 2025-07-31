from itertools import combinations
 
T = int(input())
for t in range(1, T + 1):
    def sol():
        D, W, K = map(int, input().split())
        films = [''.join(input().split()) for _ in range(D)]
        col_films = [int(''.join(col), 2) for col in zip(*films)]
 
        for film in col_films:
            if any(check in bin(film)[2:].zfill(D) for check in ('0'*K, '1'*K)):
                continue
            break
        else :
            print(f"#{t} 0")
            return
             
        for medi in range(1, K + 1):
            for comb in combinations(range(D), medi):
                for mask in range(1 << medi):
                    mask0 = mask1 = 0
                    for idx, row in enumerate(comb):
                        if (mask >> idx) & 1:
                            mask1 |= 1 << row    # B
                        else:
                            mask0 |= 1 << row    # A
                    for film in col_films:
                        new_film = (film & ~mask0) | mask1
                        if not any(check in bin(new_film)[2:].zfill(D) for check in ('0'*K, '1'*K)):
                            break
                    else:
                        print(f"#{t} {medi}")
                        return
        print(f"#{t} {K}")
    sol()