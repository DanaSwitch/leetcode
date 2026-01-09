# python3基础语法

## 错题

return返回不需要加括号



## % / //

> %取余
>
> //整除
>
> /普通除法，返回浮点数

```python
print(10 // 3)   # 输出：3 (10 ÷ 3 = 3.333... → 向下取整为3)
print(10 / 3)    # 输出：3.3333333333333335 (浮点数)
print(10 % 3)    # 输出：1 (余数)
```



## lambda表达式

```python
# 普通函数定义
def add(x, y):
    return x + y

# lambda等价写法
add_lambda = lambda x, y: x + y

print(add(3, 5))         # 输出：8
print(add_lambda(3, 5))  # 输出：8
```



## defaultdict

> `defaultdict` 是Python `collections`模块中的一个**容器数据类型**，它**提供默认值给不存在的键**，避免`KeyError`异常。

```python
from collections import defaultdict

# 创建defaultdict
dd = defaultdict(default_factory)
```

### 1.默认值为整数 (`int`) - 用于计数

```python
from collections import defaultdict

# 字符频率统计
text = "hello world"
char_count = defaultdict(int)

for char in text:
    if char != ' ':  # 跳过空格
        char_count[char] += 1  # 自动处理不存在的键

print(dict(char_count))
# 输出：{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

### 2. **默认值为列表 (`list`) - 用于分组**

```python
# 按首字母分组单词
words = ["apple", "banana", "apricot", "cherry", "blueberry"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# 输出：{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

## len

**`len()`** 是Python内置函数，用于**获取容器（如列表、字符串等）的长度或元素个数**。

```python
# 获取列表长度（元素个数）
arr = [1, 2, 3, 4, 5]
n = len(arr)  # n = 5
```

## range

用于循环控制

```python
range(stop)             # 0 到 stop-1
range(start, stop)      # start 到 stop-1  
range(start, stop, step) # 从start开始，步长为step

#最常用
n = 5
for i in range(n):  # i = 0, 1, 2, 3, 4
    print(i, end=" ")
# 输出：0 1 2 3 4

# range(start, stop)
for i in range(2, 7):  # i = 2, 3, 4, 5, 6
    print(i, end=" ")
# 输出：2 3 4 5 6

# range(start, stop, step)
for i in range(0, 10, 2):  # i = 0, 2, 4, 6, 8
    print(i, end=" ")
# 输出：0 2 4 6 8

for i in range(10, 0, -2):  # 负数步长，递减
    print(i, end=" ")
# 输出：10 8 6 4 2
```



## 转换大小写

```python
# 判断两个字符串是否相同（忽略大小写）
str1 = "Hello"
str2 = "HELLO"

if str1.lower() == str2.lower()://转化为小写
#strl.upper() 全部变大写
    print("两个字符串相同（忽略大小写）")
else:
    print("不同")

# 输出：两个字符串相同（忽略大小写）
```



## python条件表达式

```python
return ... if ... else ...

  
# 258各位相加    
    class Solution:
def addDigits(self, num: int) -> int:
return (num- 1) % 9 + 1 if num else 0

//条件判断,if cntx > only_x,则need_x = cntx - only_x, 否则need_X = 0;
need_x = cntx - only_x if cntx > only_x else 0
```



## 位运算

```python
# 假设 a = 10 (二进制 1010), b = 12 (二进制 1100)

# 按位与 &
print(f"10 & 12 = {10 & 12}")      # 输出：8  (1010 & 1100 = 1000)
# 1010 = 10
# 1100 = 12
# ----
# 1000 = 8  (只有两个都是1的位置才得1)

# 按位或 |
print(f"10 | 12 = {10 | 12}")      # 输出：14 (1010 | 1100 = 1110)

# 按位异或 ^
print(f"10 ^ 12 = {10 ^ 12}")      # 输出：6  (1010 ^ 1100 = 0110)

# 按位取反 ~
print(f"~10 = {~10}")              # 输出：-11 (注意：是补码表示)

# 左移 <<
print(f"10 << 2 = {10 << 2}")      # 输出：40 (1010 << 2 = 101000 = 40)

# 右移 >>
print(f"10 >> 1 = {10 >> 1}")      # 输出：5  (1010 >> 1 = 0101 = 5)
```

