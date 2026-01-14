# python3基础语法

## 错题

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

## range循环控制

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

