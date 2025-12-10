ans = []
for i in range(1, int(input()) + 1):
    cnt = 0
    for s in str(i):
        if s in ['3', '6', '9']:
            cnt += 1
    if cnt:
        ans.append('-' * cnt)
    else :
        ans.append(i)
print(*ans)