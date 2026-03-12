def find_less(lines):
    n = len(lines)
    stack = []
    price = list(lines)  # 浅拷贝, 两个对象, 不写的话, 改变其中一个, 另一个也会变
    # 找右侧最近的更小值
    for i in range(n-1, -1, -1):
        # 淘汰掉比自己大的
        while stack and lines[stack[-1]] >= lines[i]:
            stack.pop()
        if stack:
            price[i] = lines[stack[-1]] + lines[i] # 加上刚好比i小的
        stack.append(i)
    return price

def solve():
    lines = list(map(int, input().strip().split()))
    m = len(lines)
    lines = lines * 2  # 展开圆形
    price = find_less(lines)
    print(*price[:m])

if __name__ == "__main__":
    solve()