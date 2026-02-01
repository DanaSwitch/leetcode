"""
------------------------------------------------------------------------------
题目名称: 服务失效判断 / 寻找符合条件的最长连续子数组
文件名称: LongestLowFailurePeriod.py

【题目描述】
服务之间交换的接口成功率作为服务调用关键质量特性，某个时间段内的接口失败率使用一个数组表示。
数组中每个元素都是单位时间内失败率数值，数组中的数值为 0~100 的整数。
给定一个数值 (minAverageLost) 表示某个时间段内平均失败率容忍值，即平均失败率小于等于 minAverageLost。
找出数组中最长时间段，如果未找到则直接返回 NULL。

【输入描述】
第一行: minAverageLost (容忍值)
第二行: 数组元素 (空格分隔)
(minAverageLost 及数组中元素取值范围为 0~100 的整数，数组元素个数不超过 100 个)

【输出描述】
找出平均值 <= minAverageLost 的最长时间段。
输出数组下标对，格式 {beginIndex}-{endIndex} (下标从 0 开始)。
如果同时存在多个最长时间段，则输出多个下标对且下标对之间使用空格拼接，多个下标对按下标从小到大排序。

【示例 1】
输入:
2
0 0 100 2 2 99 0 2
输出:
0-1 3-4 6-7
解释: 
[0,0] 平均值为0 <= 2, 长度2
[2,2] 平均值为2 <= 2, 长度2
[0,2] 平均值为1 <= 2, 长度2
...最终筛选出最长的长度为2的片段有三段。

【解题思路: 前缀和优化 (Prefix Sum)】
1. 核心问题: 需要频繁计算子数组 sum(nums[i...j]) 的和来求平均值。
2. 暴力法痛点: 每次计算区间和需要遍历，整体复杂度 O(N^3)。
3. 优化策略: 
   - 构建前缀和数组 pre_sum, 其中 pre_sum[k] 表示前 k 个元素的和。
   - 区间 nums[i...j] 的和可以在 O(1) 时间内通过 pre_sum[j+1] - pre_sum[i] 得到。
   - 整体时间复杂度降低为 O(N^2)，适合本题 N <= 100 的规模。
4. 精度技巧: 
   - 判断 avg <= k 时，将其转换为 sum <= k * len。
   - 避免浮点数除法带来的精度误差。

【复杂度】
时间复杂度: O(N^2) - 需枚举所有子数组
空间复杂度: O(N)   - 用于存储前缀和数组
------------------------------------------------------------------------------
"""
import sys #导入系统库, stdin工具箱读取数据, input()是一个个读取, readline是读取一行
#readline和strip一起搭配用, readline读取会读取换行\n, strip会删掉空格,换行


class Solution:
    def main(self):
        # 1. 读取输入
        try:
            line1 = sys.stdin.readline().strip() #输入minAverageLost
            if not line1: # minAverageLost为空
                return
            min_avg_lost = int(line1)
            line2 = sys.stdin.readline().strip() #输入数组
            if not line2: # 数组为空, 程序的生命周期管理
                return
            nums = list(map(int, line2.split()))#split 切割空格
        except ValueError: # 格式不对, 直接返回
            return

        n = len(nums)
        if n == 0: # 业务逻辑管理, 空数组则返回NULL
            print("NULL")
            return

        # 2. 构建前缀和数组 (PreSum)
        # pre_sum[i] 表示 nums[0] 到 nums[i-1] 的和
        # 数组长度为 n+1，pre_sum[0] 默认为 0
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        max_len = 0
        result_list = []

        # 3. 双指针遍历所有可能的子数组
        for i in range(n):
            for j in range(i, n):
                # 利用前缀和快速计算 nums[i...j] 的区间和
                # 公式: Sum(i, j) = pre_sum[j+1] - pre_sum[i]
                current_sum = pre_sum[j + 1] - pre_sum[i]
                current_len = j - i + 1
                # 判断条件: 平均值 <= min_avg_lost
                # 变换为乘法: Sum <= min_avg_lost * len
                if current_sum <= min_avg_lost * current_len:
                    if current_len > max_len: #更新满足条件的最长时间段
                        # 发现更长的片段，清空旧结果，记录新结果
                        max_len = current_len
                        result_list = [(i, j)]
                    elif current_len == max_len:
                        # 发现同等长度的片段，追加记录
                        result_list.append((i, j))

        # 4. 输出结果
        if not result_list:
            print("NULL")
        else:
            # 题目要求按坐标从小到大排序，循环顺序保证了下标 i 从小到大
            res_strings = [f"{start}-{end}" for start, end in result_list]
            print(" ".join(res_strings))


if __name__ == "__main__":
    Solution().main()