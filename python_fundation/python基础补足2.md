### continue和break

continue 是跳过本次循环，if后面的代码都不执行，开启下一次循环

```python
for L in range(max_val, total_sum + 1):
    if total_sum % L != 0:
        continue
```



break就是直接结束这个循环

```python
# 尝试连接现有顺子
for sequence in grouped:
    if rank_map[current_card] - rank_map[sequence[-1]] == 1:  # 新牌比最后一个牌大1
        sequence.append(current_card)  # 在当前列表添加
        is_extended = True
        break
```



**`return`**：彻底结束整个函数（最干脆利落）





### sorted()排序

nums = sorted(list(map(int, input().split())))





### 字典的三个方法

| **方法**        | **返回内容**         | **例子**                          |
| --------------- | -------------------- | --------------------------------- |
| **`.keys()`**   | 所有的键（ID）       | `[1, 5]`                          |
| **`.values()`** | 所有的值（数据列表） | `[[200, 90], [5, 80]]`            |
| **`.items()`**  | **所有的键 + 值**    | `[(1, [200, 90]), (5, [50, 80])]` |



同时取出字典的键和值：

```python
for item_id, info in low_price_map.items():
    total_qty, original_price = info
    final_price = original_price
```



#### 判断键(状态)在不在字典里面

```python
memo = {}
if key in memo:
	res = memo[key]
```







### append 和 pop

遵循”后进先出“的原则：

> append(gem[i]) 是将元素放在列表的最后面，selected.pop() 是将最后一个元素弹出来





### 转化为二进制

bin(n)   就是将n转化为二进制字符串

> 当你调用 `bin(10)` 时，Python 会返回一个字符串 `'0b1010'`。
>
> `[2:]`（切片操作）
>
> 因为我们通常只需要二进制的**数值部分**，不需要前面的 `0b` 标记。

s = bin(n)[2:]   # 切掉前面的0x字符





### defaultdict

comment = defaultdict(list)    # 键不存在，自动创建空列表

cnt_digits = defaultdict(int) #键如果不存在, 自动创建0, 默认当0处理

PO2 = defaultdict(lambda: [0, 0])  # 价格低于等于100

> 这里写lambda是因为defaultdict要处理的是一个函数，lambda是匿名函数



### global和nonlocal

#### 核心区别对照表

| **特性**     | **global**                     | **nonlocal**                        |
| ------------ | ------------------------------ | ----------------------------------- |
| **指向目标** | 全局作用域（模块最外层）       | 嵌套函数（父级或更高层函数）        |
| **定义位置** | 变量在函数外部定义             | 变量在嵌套的外部函数内定义          |
| **适用场景** | 需要在函数内修改全局常量或配置 | 闭包（Closure）或递归函数中共享状态 |



### list和deque

list是栈，先进后出

deque是队列，先进先出

```python
nums = [0,1,2]
```

