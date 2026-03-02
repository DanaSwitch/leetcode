# 定义一个类，用来打包存储零件的两个属性：可靠性和价格
class Device:
    def __init__(self, reliability, price):
        self.reliability = reliability  # 可靠性
        self.price = price              # 价格

# --- 第一部分：数据读取与分类 ---
s, n = map(int, input().split())  # s:总预算, n:必须买齐的零件种类数
total = int(input())              # total:市场上零件的总个数

# reliabilities 用于记录市面上出现过的所有可靠性数值（去重）
reliabilities = set() 

# kinds 是一个大列表，里面存了 n 个小列表，每个小列表代表一类零件
kinds = [[] for _ in range(n)] 

for _ in range(total):
    # 逐行读取零件信息：种类编号、可靠性、价格
    ty, rel, pri = map(int, input().split())
    # 把这个零件变成 Device 对象，丢进它对应的种类“桶”里
    kinds[ty].append(Device(rel, pri))
    # 记录这个可靠性数值
    reliabilities.add(rel)

# --- 第二部分：辅助查找函数 ---
def binarySearch(kind, target):
    """
    在一种零件里找可靠性刚好等于 target 的零件。
    如果找不到，就返回它应该待的位置（变负数），方便后面找“大于 target 的最小值”。
    """
    low = 0
    high = len(kind) - 1
    while low <= high:
        mid = (low + high) // 2  # 相当于 (low + high) // 2
        if kind[mid].reliability > target:
            high = mid - 1
        elif kind[mid].reliability < target:
            low = mid + 1
        else:
            return mid  # 运气好，刚好找到了可靠性一样的
    return -low - 1  # 没找到，返回 -(插入位置)-1

# --- 第三部分：核心校验逻辑 ---
def check(target_reliability):
    """
    【核心】测试：如果我们要求所有零件的可靠性都必须 >= target_reliability,
    我们能不能在预算 s 之内买齐所有种类的零件？
    """
    sumPrice = 0  # 累计总花费
    for kind in kinds:
        # 在这一类零件里找可靠性 >= 目标的零件
        idx = binarySearch(kind, target_reliability)
        
        # 如果 idx 是负数，说明没找到相等的，我们要取比它大的那一个
        if idx < 0:
            idx = -idx - 1  # 这就是第一个可靠性大于目标的零件索引
        
        # 如果索引超出了零件个数，说明这一类里所有零件的可靠性都不达标
        if idx == len(kind):
            return False 
            
        # 加上这一类里最便宜且合格的零件价格
        sumPrice += kind[idx].price

    # 最后看总钱数超没超预算
    return sumPrice <= s

# --- 第四部分：主算法 ---
def getResult():
    # 1. 先把每一类零件按可靠性从小到大排好队
    # 重点：题目说了“可靠性越高越贵”，所以排好后，我们找到的第一个合格品就是最便宜的。
    for kind in kinds:
        kind.sort(key=lambda x: x.reliability)

    # 2. 把所有可靠性数值拿出来，从小到大排好，作为我们“猜”的范围
    maybe = sorted(list(reliabilities))
    
    ans = -1
    low = 0
    high = len(maybe) - 1
    
    # 3. 开始二分查找：在“可能的可靠性”列表里找最大值
    while low <= high:
        mid = (low + high) // 1
        # 如果能以 maybe[mid] 的可靠性标准买齐零件
        if check(maybe[mid]): #如果这个mid可行, 则尝试增大可靠性试试
            ans = maybe[mid]  # 记录这个可行的答案
            low = mid + 1     # 贪心：尝试更高的可靠性
        else:
            high = mid - 1    # 不行，太贵了，降低标准
            
    return ans

# 执行并打印最终结果
print(getResult())