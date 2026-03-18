import math
import sys

# 满减
def manjian(m, price):
    used = min(price // 100, m)
    return price - used * 10, used

# 打折
def dazhe(m, price):
    used = min(1, m)
    return math.floor(price * (0.92 ** used)), used

# 无门槛
def wumenkan(m, price):
    used = min(price // 5, m)
    return price - used * 5, used

def main():
    # 读取满减、打折、无门槛优惠券的数量
    manjian_count, dazhe_count, wumenkan_count = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().strip())  # 读取商品个数

    for _ in range(n):
        tmp = int(sys.stdin.readline().strip())
        final_price = tmp
        min_count = 0  # 记录最少使用的优惠券数量

        # 遍历所有两两组合
        for first, second in [(manjian, dazhe), (dazhe, manjian), 
                              (manjian, wumenkan), (wumenkan, manjian), 
                              (dazhe, wumenkan), (wumenkan, dazhe)]:
            # 先使用第一种优惠
            res1, c1 = first(manjian_count if first == manjian else dazhe_count if first == dazhe else wumenkan_count, tmp)
            # 再使用第二种优惠
            res2, c2 = second(dazhe_count if second == dazhe else manjian_count if second == manjian else wumenkan_count, res1)
            
            # 选择最优价格和最少使用的优惠券数量
            if res2 < final_price:
                final_price, min_count = res2, c1 + c2
            elif res2 == final_price:
                min_count = min(min_count, c1 + c2)

        print(final_price, min_count)

if __name__ == "__main__":
    main()