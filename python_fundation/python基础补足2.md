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



`dict.get(key, default)` 是一个非常实用且安全的方法。

简单来说，它的作用是：**“如果字典里有这个键，就给我对应的值；如果没找到，就返回我设定的那个‘默认值’。”**

```python
children = next_tasks.get(father, [])
```



```python
records = {}
...
records.setdefault(cards, []) # 检查字典是否存在键cards, 没有的话就初始化空列表[]
```





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





### s.replace(old, new, count)

- **`m.group()`**：这是 `old`（旧内容）。它就是当前被 `re.search` 找到的那一小段匹配项（例如 `"7#6"`）。
- **`str(4\*x + 3\*y + 2)`**：这是 `new`（新内容）。因为 `replace` 只能处理字符串，所以必须把计算出来的数字结果 `int` 转换成 `str`。
- **`1`**：这是 `count`（次数限制）。它规定**从左到右只替换第 1 次出现的匹配项**。





### re.serach() 和 re.group()

##### 1. `re.search()`：定位工具

- **作用：** 在字符串中扫描，找到与正则匹配的**第一个**子串。
- **返回值：**
  - 匹配成功：返回一个 **Match 对象**（包含位置、文本等信息）。
  - 匹配失败：返回 `None`。
- **特性：** 找到即停，不是必须从头匹配，只要字符串里有符合的就行。
- **核心点：** 它是整个流程的“哨兵”，负责判断是否还有符合正则的内容。

##### 2. `match_object.group()`：提取工具

- **作用：** 从 `re.search()` 返回的 **Match 对象**中，按规则提取文本。
- **语法与编号规则：**
  - `group(0)` 或 `group()`：提取**整个**匹配到的字符串。
  - `group(1)`：提取正则表达式中**第 1 个括号 `()`** 里的内容。
  - `group(2)`：提取正则表达式中**第 2 个括号 `()`** 里的内容。
- **核心点：** 没有括号 `()` 就没有 `group(n)`；它只能在 `search()` 成功拿到对象后调用。

---

**流程：** > `m = re.search(r'(正则1)#(正则2)', s)`

**逻辑：** > 1. 如果 `m` 有值 -> 成功找到！ 2. `m.group(1)` -> 拿到 `#` 左边的。 3. `m.group(2)` -> 拿到 `#` 右边的。 4. `m.group()` -> 拿到整个 `x#y`（方便用来替换）。



### 一直读的输入处理

```python
for line in sys.stdin:  # 一直读, 按行处理, 至到手动结束
    line = line.strip()
    if not line:
        continue
    time, card, state = line.split()
```





两行一起读

```python
for lines in sys.stdin:
    n, m = map(int, lines.split())
    cards = list(map(int, sys.stdin.readline().strip().split()))
```

