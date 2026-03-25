import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())  # 长度, k值
    nums = list(map(int, sys.stdin.readline().split()))

    # 绝对不满足
    if k <= 0:
        print(0)
        return

    # 统计窗口内各个数字出现次数
    num_count = defaultdict(int)
    left = 0
    ans = 0
    valid = 0  # 当前窗口中恰好达到k次的不同元素数量

    for right in range(n):
        x = nums[right]
        num_count[x] += 1
        if num_count[x] == k:
            valid += 1

        # 只要窗口有效, 就把以当前 right 结尾的所有满足子数组计入, 然后收缩左边
        while valid > 0:
            ans += n - right  # right右边的肯定也满足
            # 收缩左指针, 更新valid
            y = nums[left]
            num_count[y] -= 1
            if num_count[y] == k - 1:
                valid -= 1
            left += 1

    print(ans)

if __name__ == "__main__":
    main()