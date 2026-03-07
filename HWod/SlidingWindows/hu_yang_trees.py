import sys

# 1. 读取所有输入数据
# sys.stdin.read() 会一次性读入所有文本
# .split() 会自动把换行符、空格都切掉，变成一个纯字符串列表
raw_data = sys.stdin.read().split()

if not raw_data:
    # 如果没有输入数据，直接结束
    sys.exit(0)

# 把所有字符串转换成整数，方便后面计算
# map(int, raw_data) 意思是对 raw_data 里的每一个元素都执行 int() 操作
data = list(map(int, raw_data))

# 2. 按题目顺序解析变量
# data[0] 是 N (总数)
n = data[0]

# data[1] 是 M (未成活树的数量)
m = data[1]

# 接下来 M 个数是未成活树的编号
# 在列表 data 中，位置是 从 2 开始，一直取 M 个
# 这里的切片语法 [2 : 2+m] 意思是：从下标2开始取，取到 2+m 之前
dead_indices = data[2 : 2+m]

# 最后一个数是 K (最多补种数量)
# 它的位置刚好在死树列表的后面，也就是 2+m 这个位置
k = data[2 + m]

# ----------------- 下面是核心逻辑（和之前一样，但去掉了复杂的包装） -----------------

# 特殊情况：如果能补种的数量 K 大于等于死树的数量 M
# 说明所有死树都能救活，那么所有树都连续了
if k >= m:
    print(n)
else:
    # 为了方便计算，我们在死树列表的开头加个 0，结尾加个 N+1
    # 0 代表第1棵树左边的边界
    # n+1 代表最后一棵树右边的边界
    augmented_deads = [0] + dead_indices + [n + 1]

    max_len = 0

    # 滑动窗口计算
    # 我们要计算的是：跨越 K 个死树后，两端死树之间的距离
    # 比如补种 K=1 棵，我们就要看 第 i 个死树 和 第 i+2 个死树 之间隔了多远
    
    # 循环次数：只要保证右边的边界不超出数组范围即可
    # len(augmented_deads) 是 m+2
    # 我们需要取 augmented_deads[i + k + 1]，所以 i + k + 1 必须小于 m + 2
    for i in range(m - k + 1):
        left_boundary = augmented_deads[i]
        right_boundary = augmented_deads[i + k + 1]
        
        # 两个边界之间的活树数量 = 右边界 - 左边界 - 1
        current_len = right_boundary - left_boundary - 1
        max_len = max(max_len, current_len)

    print(max_len)