n = int(input())

lights = list(map(int, input().split()))

def solve():
    area = []
    for i in range(n):
        centre = i*100
        area.append([centre - lights[i], centre + lights[i]])
    
    area.sort(key = lambda x: (x[0], -x[1]))

    ans = 0  # 无法照明的长度

    t = area[0][1]  # 上一个照明区域的右边界
    # 遍历照明区域, 重合则覆盖, 不重合记录未照明区域
    for i in range(1, n):
        start, end = area[i]
        if t >= start:
            t = max(end, t)
        else:
            ans += start -t
            t = end
    return ans

print(solve())