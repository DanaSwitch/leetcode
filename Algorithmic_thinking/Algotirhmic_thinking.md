# 算法思想积累

## 一.倍增法快速查找二分查找上界

```python
high = 1
while not check(high):
    high <<= 1  # high *= 2
"""
先检查 k=1 是否满足
如果不满足，检查 k=2
再不满足，检查 k=4
然后 k=8，k=16，k=32...
直到找到第一个满足条件的k
"""
```

**为什么不用一个很大的固定上界？**

比如直接设置 `high = 2*10^9`？

> 1. **效率**：如果实际答案很小（比如1000），我们没必要从2e9开始二分
> 2. **准确性**：如果设置的固定上界不够大，可能找不到解
> 3. **智能性**：倍增法自动适应不同的数据规模





## 二.初始化技巧

想找最小值的话，初始值设为无穷大；想找最大值时，初始值设被负无穷大。

```python
# 找最小值
min_value = float('inf')  # 初始化为无穷大
for num in numbers:
    if num < min_value:   # 第一个数肯定比无穷大小
        min_value = num   # 更新最小值

# 找最大值  
max_value = float('-inf')  # 初始化为负无穷大
for num in numbers:
    if num > max_value:    # 第一个数肯定比负无穷大大
        max_value = num    # 更新最大值
```

