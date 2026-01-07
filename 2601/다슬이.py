import sys
sys.stdin = open("input.txt", "r")

  
# 파일 입력 관련 코드 제거함
# sys 모듈 제거함

T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())

    parent = list(range(N + 1))
    size = [1] * (N + 1)
    
    pay = [0] * (N + 1)
    real_boss = [0] * (N + 1)
    
    pay[0] = int(input().strip())

    for i in range(1, N + 1):
        my_pay, my_boss = map(int, input().strip().split())
        pay[i] = my_pay
        real_boss[i] = my_boss
    
    answer = 0
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parent[rootA] = rootB
            size[rootB] += size[rootA]
    
    for i in range(1, N + 1):
        curr = i 
        
        while True:
            if curr == 0:
                break

            boss = real_boss[curr]
            
            root_boss = find(boss)
            
            if pay[root_boss] < pay[curr]:
                pay[root_boss] = pay[curr]
                answer += size[root_boss]
                union(curr, root_boss)
                curr = root_boss
            else:
                break
                
    print(f"#{tc} {answer}")