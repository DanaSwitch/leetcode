import sys

def solve():
    lines = sys.stdin.readline().strip().split()
    if not lines:
        return
    n, m = int(lines[0]), int(lines[1])
    rules = list(map(int, sys.stdin.readline().split()))
    martix = []
    for _ in range(n):
        martix.append(list(map(int, sys.stdin.readline().split())))
    def sort_key(martix):
        return tuple(-martix[i] if rules[i] == 1 else martix[i] for i in range(m))
    
    martix.sort(key = sort_key)
    for row in martix:  # 按行输出
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()