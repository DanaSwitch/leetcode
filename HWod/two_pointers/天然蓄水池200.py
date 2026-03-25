def main():
    """
    主函数: 计算X星蓄水库的最优边界和最大蓄水量
    """
    # 读取输入
    heights = list(map(int, input().split()))
    n = len(heights)
    
    # 计算i点左侧最大高度, 不包括i
    left = [0] * n
    for i in range(1, n): #stop是开区间
        left[i] = max(left[i - 1], heights[i - 1])
    
    # 计算i点右侧最大高度, 不包括i
    right = [0] * n
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], heights[i + 1])
    
    # 计算每个位置的最高水位线
    water_line = [0] * n
    water_levels = set()
    
    for i in range(1, n - 1):
        # water是水深, 不存在合理边界(装不了水)就输出0
        water = max(0, min(left[i], right[i]) - heights[i])
        if water > 0:
            water_line[i] = water + heights[i] # 计算每个位置水位能达到的最大高度
            water_levels.add(water_line[i])
    
    # 初始化结果 [左边界, 右边界, 最大蓄水量]
    res = [0, 0, 0]
    
    # 遍历每个可能的水位线
    for level in sorted(water_levels):
        # 找左边界：从左向右找第一个满足条件的位置
        l = 0
        while l < n and (water_line[l] < level or heights[l] >= level):
            l += 1
        
        # 找右边界：从右向左找第一个满足条件的位置
        r = n - 1
        while r >= 0 and (water_line[r] < level or heights[r] >= level):
            r -= 1
        
        # 计算这个水位线下的总蓄水量
        sum_water = sum(max(0, level - heights[i]) for i in range(l, r + 1))
        
        # 更新最优结果（蓄水量更大，或蓄水量相同但距离更小）
        if sum_water > res[2] or (sum_water == res[2] and (r - l + 1) < (res[1] - res[0] + 1)):
            res = [l - 1, r + 1, sum_water]
    
    # 输出结果
    print("0" if res[2] == 0 else f"{res[0]} {res[1]}:{res[2]}")


# 程序入口
if __name__ == "__main__":
    main()