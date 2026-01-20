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
water_levels = set() # set()初始化集合, 会自动动态管理内存空间

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