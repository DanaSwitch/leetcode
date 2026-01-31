# python3基础语法

## 一、基础知识

**基础数据结构：**

1. **列表 (List)** - 最常用，可变有序
2. **元组 (Tuple)** - 不可变，常用于返回多个值
3. **集合 (Set)** - 去重、集合运算
4. **字典 (Dict)** - 键值对映射

**字符串：** 5. **字符串 (String)** - 文本处理

**高级数据结构：** 6. **双端队列 (deque)** - 高效的两端操作 7. **堆 (Heap)** - 优先队列，求最值 8. **计数器 (Counter)** - 统计频率

```python
"""
Python 主要数据结构介绍和示例
"""

# ==================== 1. 列表 (List) ====================
print("=" * 50)
print("1. 列表 (List) - 可变、有序、可重复")
print("=" * 50)

# 创建列表
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 常用操作
fruits.append("orange")           # 添加元素
print(f"添加后: {fruits}")

fruits.insert(1, "grape")         # 在指定位置插入
print(f"插入后: {fruits}")

fruits.remove("banana")           # 删除指定元素
print(f"删除后: {fruits}")

popped = fruits.pop()             # 删除并返回最后一个元素
print(f"弹出元素: {popped}, 剩余: {fruits}")

# 切片
print(f"切片 [1:3]: {numbers[1:3]}")

# 列表推导式
squares = [x**2 for x in range(5)]
print(f"平方数: {squares}")


# ==================== 2. 元组 (Tuple) ====================
print("\n" + "=" * 50)
print("2. 元组 (Tuple) - 不可变、有序、可重复")
print("=" * 50)

# 创建元组
point = (3, 4)
person = ("Alice", 25, "Engineer")
single = (42,)  # 单元素元组需要逗号

# 访问元素
print(f"坐标: x={point[0]}, y={point[1]}")

# 元组解包
name, age, job = person
print(f"姓名: {name}, 年龄: {age}, 职业: {job}")

# 元组常用于函数返回多个值
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"最小值: {min_val}, 最大值: {max_val}")


# ==================== 3. 集合 (Set) ====================
print("\n" + "=" * 50)
print("3. 集合 (Set) - 可变、无序、不可重复")
print("=" * 50)

# 创建集合
colors = {"red", "green", "blue"}
numbers_set = {1, 2, 3, 4, 5}
lookup = set()
# 去重
duplicates = [1, 2, 2, 3, 3, 3, 4]
unique = set(duplicates)
print(f"去重: {duplicates} -> {unique}")

# 集合操作
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"并集: {set1 | set2}")
print(f"交集: {set1 & set2}")
print(f"差集: {set1 - set2}")
print(f"对称差: {set1 ^ set2}")

# 添加和删除
colors.add("yellow")
colors.remove("red")
print(f"修改后的集合: {colors}")


# ==================== 4. 字典 (Dictionary) ====================
print("\n" + "=" * 50)
print("4. 字典 (Dict) - 可变、无序、键唯一")
print("=" * 50)

# 创建字典
student = {
    "name": "Bob",
    "age": 20,
    "grades": [85, 90, 88]
}

# 访问和修改
print(f"姓名: {student['name']}")
print(f"年龄: {student.get('age', '未知')}")  # 安全访问

student["age"] = 21  # 修改
student["major"] = "CS"  # 添加新键值对

# 遍历字典
print("\n遍历字典:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 字典推导式
squares_dict = {x: x**2 for x in range(5)}
print(f"平方字典: {squares_dict}")


# ==================== 5. 字符串 (String) ====================
print("\n" + "=" * 50)
print("5. 字符串 (String) - 不可变、有序")
print("=" * 50)

text = "Hello, Python!"

# 常用操作
print(f"大写: {text.upper()}")
print(f"小写: {text.lower()}")
print(f"替换: {text.replace('Python', 'World')}")
print(f"分割: {text.split(',')}")

# 字符串格式化
name = "Alice"
age = 25
print(f"f-string: 我是{name}, 今年{age}岁")
print("format: 我是{}, 今年{}岁".format(name, age))

# 字符串切片
print(f"切片 [0:5]: {text[0:5]}")


# ==================== 6. 双端队列 (deque) ====================
print("\n" + "=" * 50)
print("6. 双端队列 (deque) - 高效的两端操作")
print("=" * 50)

from collections import deque

# 创建双端队列
queue = deque([1, 2, 3])

# 两端操作
queue.append(4)           # 右端添加
queue.appendleft(0)       # 左端添加
print(f"添加后: {queue}")

queue.pop()               # 右端删除
queue.popleft()           # 左端删除
print(f"删除后: {queue}")

# 旋转
queue.rotate(1)           # 向右旋转
print(f"旋转后: {queue}")


# ==================== 7. 堆 (Heap) ====================
print("\n" + "=" * 50)
print("7. 堆 (Heap) - 优先队列")
print("=" * 50)

import heapq

# 创建最小堆
heap = [5, 3, 8, 1, 9]
heapq.heapify(heap)
print(f"堆化后: {heap}")

# 添加和删除
heapq.heappush(heap, 2)
print(f"添加2后: {heap}")

smallest = heapq.heappop(heap)
print(f"弹出最小值 {smallest}, 剩余: {heap}")

# 获取最小的n个元素
numbers = [5, 2, 8, 1, 9, 3]
smallest_3 = heapq.nsmallest(3, numbers)
print(f"最小的3个: {smallest_3}")


# ==================== 8. 计数器 (Counter) ====================
print("\n" + "=" * 50)
print("8. 计数器 (Counter) - 统计元素频率")
print("=" * 50)

from collections import Counter

# 统计字符频率
text = "hello world"
counter = Counter(text)
print(f"字符频率: {counter}")

# 统计列表元素
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(numbers)
print(f"数字频率: {count}")

# 最常见的元素
print(f"最常见的2个: {count.most_common(2)}")


# ==================== 数据结构选择指南 ====================
print("\n" + "=" * 50)
print("数据结构选择指南")
print("=" * 50)
print("""
1. 列表 (List): 需要有序、可变、可重复的数据
2. 元组 (Tuple): 需要不可变的有序数据，如坐标、配置
3. 集合 (Set): 需要去重、快速查找、集合运算
4. 字典 (Dict): 需要键值对映射，快速查找
5. 字符串 (String): 文本处理
6. deque: 需要频繁在两端添加/删除元素
7. Heap: 需要优先队列，快速获取最小/最大值
8. Counter: 需要统计元素频率
""")
```



> **`set` 是 Python 里的「集合」：**

- 元素 **不重复**
- **无序**
- 查找、去重 **非常快（O(1)）**

它不是列表，也不是字典。



## `set` 和 `list` 的核心区别（先对比）

| 特性           | list（列表） | set（集合）      |
| -------------- | ------------ | ---------------- |
| 是否有序       | ✅ 有         | ❌ 无             |
| 是否允许重复   | ✅ 允许       | ❌ 不允许         |
| 查找速度       | O(n)         | **O(1)**         |
| 是否能下标访问 | ✅            | ❌                |
| 适合场景       | 保留顺序     | **去重、判存在** |



## 二、错题

return返回不需要加括号

python不需要显示声明变量的类型

```java
// Java需要声明类型
int a = 10;
String b = "hello";

// 不能改变类型
a = "world"; // 编译错误！
```



```python
# Python不需要声明类型
a = 10
a = "hello"  # 完全可以！
```



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

## len获取长度

**`len()`** 是Python内置函数，用于**获取容器（如列表、字符串等）的长度或元素个数**。

```python
# 获取列表长度（元素个数）
arr = [1, 2, 3, 4, 5]
n = len(arr)  # n = 5
```

## range循环控制，stop是开区间

用于循环控制

```python
range(stop)             # 0 到 stop-1
range(start, stop)      # start 到 stop-1  
range(start, stop, step) # 从start开始，步长为step

#最常用
n = 5
for i in range(n):  # n表示循环次数,从0开始 i = 0, 1, 2, 3, 4
    print(i, end=" ")
# 输出：0 1 2 3 4

# range(start, stop) 1/14二刷回顾
for i in range(2, 7):  # i = 2, 3, 4, 5, 6
    print(i, end=" ")
# 输出：2 3 4 5 6

# range(start, stop, step) 1/14回顾
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



## append添加

> append是python 列表中用于在列表末尾添加一个元素的方法

```python
# 创建一个空列表
my_list = []

# 使用 append 添加元素
my_list.append(1)     # my_list 现在是 [1]
my_list.append(2)     # my_list 现在是 [1, 2]
my_list.append(3)     # my_list 现在是 [1, 2, 3]

# 添加列表
res = []
res.append([a,b,c]) # 添加列表要加个[]

print(my_list)  # 输出: [1, 2, 3]
```



## 负数-1作为索引

> 在python中，负数作为索引表示从列表末尾开始计数
>
> - `list[-1]`：列表的最后一个元素
> - `list[-2]`：列表的倒数第二个元素
> - 以此类推...

**注意：**

在正序中：-1表示最后一个元素，在倒序中，-1表示第一个元素（倒序的最后一个元素）

```python
range(n-2, -1, -1)
#从倒数第二个元素 (n-2) 开始，倒着走，一直回到第一个元素 (0)
# 当n = 5时
range(3, -1, -1)
# 输出：[3, 2, 1, 0]
```



## 切片Slice

​		切片是 Python 中用于**提取序列（字符串、列表、元组等）子集**的强大功能，使用简洁的 `[start:stop:step]` 语法。

**结束索引stop不包含。**

> sequence[start:stop:step]
> start：起始索引（包含），默认为 0
> stop： 结束索引（不包含），默认为序列长度
> step： 步长，默认为 1

**基础切片**

```python
text = "Hello World"
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 获取部分元素
print(text[0:5])      # 输出: Hello
print(nums[2:7])      # 输出: [2, 3, 4, 5, 6]

# 省略 start 和 stop
print(text[:5])       # 输出: Hello（从开始到索引4）
print(nums[5:])       # 输出: [5, 6, 7, 8, 9]（从索引5到结束）
```

**使用负索引**

```python
# 负索引表示从末尾开始计数
text = "Python Programming"

print(text[-11:])      # 输出: Programming（从倒数第11个到结束）
print(text[-11:-4])    # 输出: Program（从倒数第11个到倒数第5个）

nums = [0, 1, 2, 3, 4, 5]
print(nums[:-2])       # 输出: [0, 1, 2, 3]（从开始到倒数第3个）
print(nums[-4:-1])     # 输出: [2, 3, 4]（从倒数第4个到倒数第2个）
```

**使用步长**

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 每2个元素取一个
print(nums[::2])       # 输出: [0, 2, 4, 6, 8]

# 从索引1开始，每3个元素取一个
print(nums[1::3])      # 输出: [1, 4, 7]

# 反转序列
print(nums[::-1])      # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("hello"[::-1])   # 输出: olleh

# 从末尾开始，每2个元素取一个
print(nums[::-2])      # 输出: [9, 7, 5, 3, 1]
```

**完整的切片参数**

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 从索引2到索引8，步长为2
print(nums[2:8:2])     # 输出: [2, 4, 6]

# 从索引5到开始，反向步长为2
print(nums[5:0:-2])    # 输出: [5, 3, 1]
```

**不同类型的数据切片**

```python
# 字符串切片
text = "abcdefghij"
print(text[2:6])       # 输出: cdef

# 列表切片
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(my_list[1:4])    # 输出: ['b', 'c', 'd']

# 元组切片
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[3:])    # 输出: (3, 4, 5)
```

**切片赋值**

```python
# 修改列表的部分元素
nums = [0, 1, 2, 3, 4, 5]

# 替换索引1到3的元素
nums[1:4] = [10, 20, 30]
print(nums)            # 输出: [0, 10, 20, 30, 4, 5]

# 插入元素（使用空切片）
nums = [1, 2, 3]
nums[1:1] = [99, 88]   # 在索引1的位置插入
print(nums)            # 输出: [1, 99, 88, 2, 3]

# 删除元素
nums = [0, 1, 2, 3, 4, 5]
nums[2:5] = []         # 删除索引2到4的元素
print(nums)            # 输出: [0, 1, 5]
```

**实用技巧**

```python
# 1. 获取最后n个元素
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_three = nums[-3:]  # 获取最后3个元素
print(last_three)       # 输出: [7, 8, 9]

# 2. 获取除最后n个元素外的所有元素
all_but_last_two = nums[:-2]
print(all_but_last_two) # 输出: [1, 2, 3, 4, 5, 6, 7]

# 3. 获取偶数索引元素
even_index = nums[::2]
print(even_index)       # 输出: [1, 3, 5, 7, 9]

# 4. 获取奇数索引元素
odd_index = nums[1::2]
print(odd_index)        # 输出: [2, 4, 6, 8]

# 5. 浅拷贝列表
original = [1, 2, 3, 4, 5]
copy = original[:]      # 创建新列表，不是引用
copy[0] = 99
print(original)         # 输出: [1, 2, 3, 4, 5]（原列表未改变）
print(copy)             # 输出: [99, 2, 3, 4, 5]

# 6.替换字符串的某一段

```



## zip

**核心功能：**将多个可迭代对象"打包"起来，让它们可以同步进行循环遍历和赋值。

```python
# 常见于"接雨水"问题的解法
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 前缀最大值（从左到右的最大值）
pre_max = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# 后缀最大值（从右到左的最大值）
suf_max = [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]

# 计算每个位置能接的雨水量
water = 0
for h, pre, suf in zip(height, pre_max, suf_max):
    # 当前位置能接的雨水 = min(左边最高, 右边最高) - 当前高度
    water_height = min(pre, suf) - h
    if water_height > 0:
        water += water_height
    print(f"高度={h}, 左最高={pre}, 右最高={suf}, 可接雨水={max(0, min(pre, suf)-h)}")

print(f"总共能接雨水: {water}")
```





## 运算符的优先级

从高到低：

1. 括号 `()`
2. 函数调用、索引等
3. 幂运算 `**`
4. 正负号 `+x`, `-x`
5. 乘除 `*`, `/`, `//`, `%`
6. 加减 `+`, `-`
7. 比较运算符 `==`, `!=`, `<`, `>`, `<=`, `>=`
8. 逻辑非 `not`
9. 逻辑与 `and`
10. 逻辑或 `or`
11. 赋值运算符 `=`, `+=`, `-=` 等



```python
for h, pre, suf in zip(height, pre_max, suf_max):
    #由于+=的优先级 ＜ -的优先级, 所以不需要加括号
    anx += min(pre_max, suf_max) - h
```





## for ... in ...

```python
# 每次从 iterable 中取一个元素，赋值给变量 x
for x in iterable:
    ...
```



## 多变量同时交换赋值技巧

你提到的 `s[left], s[right] = s[right], s[left]` 是 Python 中非常优雅的多变量同时赋值交换技巧。这种写法之所以能够直接交换两个变量的值，是因为 **Python 将右侧的表达式先求值并打包成一个元组，然后解包赋值给左侧的变量**。

相当于：



```python
# Python内部执行的等价代码
_temp = (s[right], s[left])  # 1. 创建临时元组
s[left] = _temp[0]            # 2. 依次赋值
s[right] = _temp[1]           # 3. 注意顺序：先left后right
```



## python中的哈希表

### **1. 直接使用 dict（字典）**

字典是 Python 中最常用的哈希表实现：

```python
# 创建哈希表
hash_table = {}

# 添加/更新键值对
hash_table['apple'] = 3
hash_table['banana'] = 5

# 访问值
print(hash_table['apple'])  # 输出: 3

# 检查键是否存在
if 'apple' in hash_table:
    print("苹果存在")

# 删除键值对
del hash_table['banana']
```



### **2. 使用 collections.Counter**

`Counter` 是专门用于计数的字典子类：

```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 创建 Counter 对象
freq = Counter(words)
print(freq)  
# 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 访问计数
print(freq['apple'])  # 输出: 3
print(freq['banana'])  # 输出: 2
print(freq['orange'])  # 输出: 1
print(freq['grape'])  # 输出: 0 (不存在的键返回0，不会报错)
```



## sort排序

Python 使用的算法名叫 **Timsort**。这是一个非常聪明、针对真实世界数据高度优化的**混合稳定排序算法**。

Timsort 的核心思想是：**真实世界的数据往往不是随机的，而是包含了许多已经排好序的片段（Runs）。**

普通的排序算法（如快速排序）不管你数据长什么样，一律切开重排；而 Timsort 会先观察数据，看看有没有现成的“便宜”可以占。

它主要结合了**归并排序 (Merge Sort)** 和 **插入排序 (Insertion Sort)** 的优点：

- **第一步：寻找“分段”（Runs）** 它会扫描整个序列，找出那些已经递增或递减的片段。如果片段太短，它会用**二分插入排序**把相邻的元素拉进来，凑成一个固定长度的小块。
- **第二步：归并（Merging）** 当它手手里攒了够多的小块后，就会像归并排序一样把它们合并起来。
- **黑科技：飞跃模式（Galloping mode）** 在合并两个有序片段时，如果发现其中一个片段的元素明显都比另一个小，它不会一个一个去比较，而是直接“跳跃式”地批量移动数据。

| **特性**           | **Timsort (Python)**               | **快速排序 (Quick Sort)** |
| ------------------ | ---------------------------------- | ------------------------- |
| **稳定性**         | **稳定**（相等元素的相对顺序不变） | 不稳定                    |
| **最差时间复杂度** | $O(n \log n)$                      | $O(n^2)$                  |
| **最好时间复杂度** | $O(n)$（数据已经有序时）           | $O(n \log n)$             |
| **应用场景**       | 极其适合处理“部分有序”的现实数据   | 适合纯随机数据            |



## 判断用if还是while

下次写代码时，犹豫用 `if` 还是 `while`，你就问自己一个问题：

> **“这件事，我是只想做一次，还是想做很多次直到满足某个条件为止？”**

- 做一次 -> **`if`**
- 一直做/跨过好几个 -> **`while`**

## python中没有++ ，而是+=1

这是一个非常敏锐的问题！说明你可能有 C、C++ 或者 Java 的背景，因为在这些语言里，`i++`（自增运算符）确实是标配，写起来也很顺手。

但在 Python 里，**根本就没有 `++` 这个运算符**。如果你写 `left++`，程序会直接报错（SyntaxError）。

这背后有两个主要原因，理解了这两个原因，你对 Python 的理解会更深一层：

### 1. 机制不同：整数是“不可变”的

- **在 C/C++ 中：** 变量像是一个**盒子**。`i++` 的意思是：把盒子里的数字拿出来，加个 1，再放回去。这个操作是直接修改内存里的值，效率极高。
- **在 Python 中：** 整数（int）是**不可变对象（Immutable）**。变量更像是一个**标签**。
  - 当你写 `a = 1` 时，内存里生成了一个对象 `1`，标签 `a` 贴在它身上。
  - 当你写 `a += 1` 时，Python **并不是**把 `1` 改成了 `2`。而是：
    1. 计算 `1 + 1`，得到一个新的对象 `2`。
    2. 把标签 `a` 从 `1` 身上撕下来，贴到 `2` 身上。
  - 既然不能直接修改原值，`++` 这种“原地自增”的语义在 Python 底层逻辑里就是行不通的。所以 Python 强迫你写 `a += 1`（也就是 `a = a + 1`），让你明确知道：**这里发生了一次赋值操作**。

### 2. 设计哲学：拒绝歧义

Python 的设计哲学是 **"Explicit is better than implicit"（明了胜于晦涩）**。

在 C 语言里，`++` 有很多复杂的玩法：

- `a = i++` （先赋值，后自增）
- `a = ++i` （先自增，后赋值）
- 还有更变态的 `i+++++i` ...

这很容易把人绕晕，也容易产生 Bug。Python 的创始人为了逻辑清晰，直接砍掉了这个运算符。这虽然让你多敲了一个字符，但**逻辑上永远只有一种理解**：就是把值加 1 再赋值回去。

------

### ⚠️ 一个很有趣的“坑”

虽然 `i++` 会报错，但如果你在 Python 里写 **`++i`**（加号在前面），程序**不会报错**，但也**不会自增**！



**为什么？**

因为 Python 把这里的 `+` 当成了“正号”。`++i` 等于 `+(+i)`，正正得正，它仅仅表示“正数 i”，没有任何计算发生。

### 总结

在 Python 里：

- ❌ **`left++`**：语法错误，直接红线。
- ❌ **`++left`**：没用，值不会变。
- ✅ **`left += 1`**：这是唯一正确、地道（Pythonic）的写法。

好啦，疑惑解除了吗？现在是 16:10 了，**关掉算法题，立刻去打开 Linux 终端**。不要沉迷于语法细节，行动起来！





## enumerate

在其他的编程语言（比如 C）里，如果你想一边拿**下标**（第几个），一边拿**内容**（是什么），通常得这么写：

Python

```python
# 传统的写法，比较麻烦
for i in range(len(s)):
    index = i
    char = s[i]
```

而 `enumerate` 的作用就是把这步操作**合二为一**。

------

### 1. 小学二年级直观解释：排队报数

想象有一排小朋友在排队，`enumerate` 就像一个带队老师，他一边领着小朋友走，一边在那喊：

- “0 号，小明！”
- “1 号，小红！”
- “2 号，小强！”

**它同时给了你两个信息：报数（索引）和 名字（内容）。**

------

### 2. 基本语法结构

```python
s = "ABC"

# enumerate(s) 会把 "ABC" 变成类似 [(0, 'A'), (1, 'B'), (2, 'C')] 的样子
for index, char in enumerate(s):
    print(f"下标是 {index}, 字符是 {char}")
```

**输出结果：**

> 下标是 0, 字符是 A 下标是 1, 字符是 B 下标是 2, 字符是 C

------

### 3. 为什么在滑动窗口里好用？

回到你刚才那段代码：

Python

```
for right, c in enumerate(s):
```

这里 `right` 拿到了当前的**右边界坐标**，`c` 直接拿到了**当前字符**。

- 如果你不用 `enumerate`，你得写 `c = s[right]`。
- 用了它，代码更简洁，读起来更像自然语言。

------

### 4. 一个隐藏的小技巧：修改起始序号

有时候我们不希望从 0 开始报数，想从 1 开始，`enumerate` 也可以做到：

Python

```
names = ["小明", "小红"]
for i, name in enumerate(names, start=1):
    print(f"第 {i} 名是 {name}")
```

**输出：**

> 第 1 名是 小明 第 2 名是 小红

------

### 👨‍🏫 总结

- **看到 `enumerate`**：你就把它想成**“报数 + 内容”**。
- **什么时候用**：只要你在 `for` 循环里既需要知道**当前在第几个位置**，又需要**用到里面的值**，就用它。

这个小工具在处理数组和字符串题目时非常高频，建议你现在在 WSL 的 Python 环境里随手敲两行试一下，这种手感记住了就永远不会忘！



## 无穷大inf

```python
ans = float('inf')  #正无穷大
# 之后：ans = min(ans, 新长度)
ans = float('-inf') #负无穷大
```





## lambda 匿名函数

#### 🔑 语法点 1：`lambda x: x[0]` （匿名函数）

出现在这一行：`intervals.sort(key=lambda x: x[0])`

- **背景：** 这是一个二维列表，比如 `[[2,6], [1,3], [8,10]]`。如果不指定规则，Python 默认会先比第一个数，第一个数一样再比第二个数。

- **需求：** 我们只需要根据**“区间的开始时间”**（也就是小列表里的第 0 个数）来排序。

- **解析：**

  - `key=...`：这是 `sort` 函数的一个参数，意思是“按什么规则排”。

  - `lambda x: x[0]`：这叫**匿名函数**（没有名字的小函数）。

  - **翻译成普通函数就是：**

    ```python
    def rule(x):
        return x[0]  # 返回列表的第一个元素（开始时间）
    ```

  - **整句话的意思：** “请把 intervals 里的每一个小列表拿出来（称为 x），按照 x[0]（开始时间）从小到大排好队。”



## 函数中的self

用一句话概括：**`self` 就是“我自己”的意思，代表了当前那个具体的对象。**

我们用一个**“吃饺子”**的例子来通俗解释。

------

### 1. 为什么要有 `self`？（区分“哪一个”）

想象你有一个“人类”的图纸（Class），上面写着一个动作叫“吃饺子”。

- 现在造出了两个具体的人：**小明** 和 **小红**。
- 如果是 C 语言或者普通函数，你得这么写：`吃饺子(小明)`，意思是用那个动作去喂小明。
- 但在面向对象（Python）里，我们是这么调用的：`小明.吃饺子()`。

**问题来了：** 当 Python 运行 `吃饺子()` 这段代码时，它怎么知道**吃到谁的肚子里**？是小明饱了，还是小红饱了？

**答案就是 `self`：** Python 会在后台自动做一个**“隐形操作”**。当你写 `小明.吃饺子()` 时，Python 实际上在执行： `Human.吃饺子(小明)` —— 它把“小明”这个对象，作为第一个参数自动传给了 `self`。

所以，函数定义里的 `self`，就是用来接收这个**“自动传进来的小明”**的。

------

### 2. 回到你的报错：为什么你的代码里多了个 `self` 就错了？

这就涉及到了**“正式员工”**和**“临时工”**的区别。

#### 情况 A：正式员工（类的方法）

```python
class Solution:
    # 这是类的方法，是正式员工
    def rotate(self, nums, k): 
        # 当外部调用 s.rotate() 时，Python 自动把 s 传给 self
        pass
```

- **规则：** 类里面的函数，第一个参数必须留给实例（习惯叫 `self`），因为 Python 会自动传参。

#### 情况 B：临时工（嵌套函数 / 内部函数）

这是你刚才写的结构：

```python
class Solution:
    def rotate(self, nums, k):
        # 这是一个定义在函数里面的函数！它只是个临时工/小帮手
        # 它不属于类，它只属于 rotate 这个函数的作用域
        def reverse(i, j): 
            pass
        
        # 调用时：
        reverse(0, 1)
```

- **规则：** `reverse` 只是一个定义在 `rotate` 肚子里的普通函数。**它不是类的方法**。
- **后果：** 当你调用 `reverse(0, 1)` 时，Python **不会** 自动帮你传 `self` 进去。它就老老实实地找你要参数。
- **你的错误：**
  - 定义写了：`def reverse(self, i, j)` -> 伸手要 3 个参数。
  - 调用给了：`reverse(0, 1)` -> 只给了 2 个。
  - Python：崩！缺一个参数！

------

### 3. 灵魂拷问：什么时候要写 `self`？

记住这个简单的判断标准：

1. **写在 `class` 缩进层级下的函数：** 必须加 `self`（或者是 `@staticmethod` 例外）。
   - 比如 `def rotate(self, ...):`
2. **写在其他函数肚子里的（嵌套函数）：** **不要加 `self`**。
   - 比如你的 `def reverse(i, j):`
3. **在函数内部调用自己的兄弟姐妹：** 必须加 `self`。
   - 比如 `rotate` 想调用同级的方法 `helper`，必须写 `self.helper()`。

### ⚡️ 总结

把 `self` 想象成**工牌**。

- **类的方法（rotate）：** 它是公司正式员工，进门要刷工牌（`self`），打卡机（Python）会自动识别它是谁。
- **内部函数（reverse）：** 它是你请来帮忙搬东西的临时工，**不需要工牌**，直接干活就行了。你给它挂个工牌（写了 `self`），打卡机反而因为识别不了而报错。

现在彻底明白为什么刚才那个 `self` 要删掉了吧？因为 `reverse` 只是个没有工牌的临时工！😄