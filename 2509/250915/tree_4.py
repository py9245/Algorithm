import sys
sys.stdin = open('input.txt', "r")

T = 10

for case in range(1, T + 1):
    class Tree:
        def __init__(self, n):
            self.tree = [None, None, None] * (n + 1)

        def inorder(self, node=1):
            value, left, right = self.tree[node]

            if value.isdigit():  # 숫자면 바로 반환
                return int(value)

            l_val = self.inorder(left)
            r_val = self.inorder(right)

            if value == '+':
                return l_val + r_val
            elif value == '-':
                return l_val - r_val
            elif value == '*':
                return l_val * r_val
            elif value == '/':
                return l_val // r_val

    N = int(input())
    tree = Tree(N)

    for _ in range(N):
        a = input().split()
        idx = int(a[0])
        value = a[1]
        if len(a) == 4:
            tree.tree[idx] = (value, int(a[2]), int(a[3]))
        else:
            tree.tree[idx] = (value, None, None)

    print(f"#{case} {tree.inorder()}")
