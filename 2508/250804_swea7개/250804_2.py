T = int(input())
 
for case in range(1, T + 1):
    N = int(input())
    print(f"#{case} {len(max(input().split('0'),key=len))}")