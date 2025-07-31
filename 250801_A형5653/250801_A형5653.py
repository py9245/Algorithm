T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())

    cell_dict = {(i, j): [num, num, num] for i in range(N) for j, num in enumerate(map(int, input().split())) if num > 0}

    dead = set()
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(K):
        new_cell = {}
        die = set()

        for key in list(cell_dict.keys()):
            act, inact, life = cell_dict[key]

            if inact > 0:
                cell_dict[key][1] -= 1
                continue

            if inact == 0:
                x, y = key
                for dx, dy in dir:
                    nk = (x + dx, y + dy)
                    if nk in cell_dict or nk in dead:
                        continue

                    if nk in new_cell:
                        if new_cell[nk][2] < life:
                            new_cell[nk] = [life, life, life]
                    else:
                        new_cell[nk] = [life, life, life]

                cell_dict[key][0] -= 1
                cell_dict[key][1] = -1

            else:  # inact < 0
                cell_dict[key][0] -= 1

            if cell_dict[key][0] == 0:
                die.add(key)

        for d in die:
            dead.add(d)
            del cell_dict[d]

        for nk, val in new_cell.items():
            if nk not in dead:
                cell_dict[nk] = val

    print(f"#{t} {len(cell_dict)}")