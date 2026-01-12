"""
1202 华为OD双机位C卷 天然蓄水池
公元2919年,人类终于发现了一颗宜居星球——X星. 
现想在X星一片连绵起伏的山脉间建一个天热蓄水库,如何选取水库边界,使蓄水量最大?

要求:

山脉用正整数数组s表示,每个元素代表山脉的高度
选取山脉上两个点作为蓄水库的边界,则边界内的区域可以蓄水,蓄水量需排除山脉占用的空间
蓄水量的高度为两边界的最小值
如果出现多个满足条件的边界,应选取距离最近的一组边界
输出边界下标(从0开始)和最大蓄水量;如果无法蓄水,则返回0,此时不返回边界.
例如,当山脉为s=[3,1,2]时,则选取s[0]和s[2]作为水库边界,则蓄水量为1,
此时输出:0 2:1 当山脉s=[3,2,1]时,不存在合理的边界,此时输出:0
输入描述:
1 9 6 2 5 4 9 3 7
输出描述: 输出的是边界下标和最大蓄水量,格式为: left right:max_water
1 6:19
"""
def main():
    # 1. 读取输入
    s = list(map(int, input().split())) #将输入的字符串分割并转换为整数列表
    n = len(s) #获取长度, 山脉数量
    
    if n < 3:
        print(0)
        return
    
    # 预处理前缀和数组，用于快速计算山脉高度和
    prefix_sum = [0] * (n + 1) #创建一个长度为n+1的前缀和数组, 并用0初始化所有元素
    for i in range(n): #从0到n-1遍历
        prefix_sum[i + 1] = prefix_sum[i] + s[i] #计算前缀和
    
    # 2. 初始化
    max_water = 0
    best_left = -1
    best_right = -1
    # 如果有多个满足条件的边界, 则选择嘴里最近的那个边界
    min_distance = float('inf') #想要找最小值, 则初始化为最大值 infinity:无穷大
      
    # 3. 双指针主循环
    # 左指针从左往右走, 从0到n-3, 循环n-2次
    for left in range(n - 2):  # 左边界最多到倒数第3个位置, 要留出右边界和中间的空位置
        # 对于每个左边界，右指针从最右边往左走, 最右边是n-1
        right = n - 1
        
        # 记录这个左边界遇到的最高的障碍山
        max_obstacle = 0
        
        while right > left + 1:  # 右边界至少要离左边界2个位置
            # 水面高度 = 两座山中较矮的
            water_height = min(s[left], s[right])
            
            # 如果水面高度 <= 之前遇到的最高障碍，肯定不能蓄水
            if water_height <= max_obstacle:
                right -= 1
                continue
            
            # 检查中间的山是否都低于水面
            can_store = True
            for k in range(left + 1, right):
                if s[k] >= water_height:
                    can_store = False
                    # 记录这个障碍山的高度
                    if s[k] > max_obstacle:
                        max_obstacle = s[k]
                    break
            
            if can_store:
                # 计算蓄水量
                total_water = 0
                for k in range(left + 1, right):
                    total_water += water_height - s[k]
                
                if total_water > 0:
                    distance = right - left
                    
                    # 更新最佳结果
                    if total_water > max_water:
                        max_water = total_water
                        best_left = left
                        best_right = right
                        min_distance = distance
                    elif total_water == max_water and distance < min_distance:
                        # 蓄水量相同时，选距离更近的
                        best_left = left
                        best_right = right
                        min_distance = distance
                
                # 尝试更小的右边界（可能距离更近）
                right -= 1
            else:
                # 不能蓄水，继续尝试更小的右边界
                right -= 1
    
    # 4. 输出结果
    if max_water > 0:
        print(f"{best_left} {best_right}:{max_water}")
    else:
        print(0)

if __name__ == "__main__":
    main()