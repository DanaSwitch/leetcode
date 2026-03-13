"""
思路: A[i]*X - B[i]
"""
raw = input().strip().split(";")
n = len(raw) - 3

def dot(A, X):
    return sum(a * b for a, b in zip(A,X))

def satisfy(result, op):
    if op == ">": return result > 0
    if op == ">=": return result >= 0
    if op == "<": return result < 0
    if op == "<=": return result <= 0
    if op == "=": return result == 0
    return False

A = [list(map(float, raw[i].split(','))) for i in range(n)]  # 二维矩阵, 外面再加个[]
X = list(map(float, raw[n].split(',')))
B = list(map(float, raw[n+1].split(',')))
ops = raw[n+2].split(',')

diff = [dot(A[i], X) - B[i] for i in range(n)]

is_valid = all(satisfy(diff[i], ops[i]) for i in range(n))

print(str(is_valid).lower(), int(max(diff)))  # 转为小写