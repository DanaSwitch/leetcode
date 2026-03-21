"""
思路: 单调栈优先放新遍历的元素, 记录弹出的元素
"""
import sys

# 找到左边小于本身高度的最近点
def find_left_small(nums):
    n = len(nums)
    left = [-1] * n
    stack = []
    for i in range(n):
        # 先淘汰掉不小于自己的
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            # 最后一个就是最近且小于自己的, 记录下来
            left[i] = stack[-1]  # 记录的i左侧最近且小于 nums[i] 的元素的下标
        stack.append(i)  # 将自己的下标记录下来
    return left

# 找到右边小于本身高度的最近点
def find_right_smaller(nums):
    n = len(nums)
    right = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):  # 从右往左递增
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

def main():
    line = sys.stdin.readline().strip()
    heights = list(map(int, line.split()))
    n = len(heights)

    # 数量小于三肯定不存在指定元组
    if n < 3:
        print(-1)
        return

    left = find_left_small(heights)
    right = find_right_smaller(heights)

    res = float("inf")
    for j in range(n):
        # 左侧小于自己最近的点
        i = left[j]
        k = right[j]
        # 左侧或右侧不存在这样的点
        if i == -1 or k == -1:
            continue
        res = min(res, k - i)

    # 输出结果
    print(-1 if res == float("inf") else res)

if __name__ == "__main__":
    main()