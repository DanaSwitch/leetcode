"""
这题就是在列表中每次取N个(窗口数), 每个窗口一个
"""
import sys
from collections import deque

number_of_rows = int(sys.stdin.readline().strip())  # 窗口个数/行
number_of_columns = int(sys.stdin.readline().strip())  # 窗口容量/列

queue_list = []

# 读取数据, 每行存入队列
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    # [deque(), deque(), ....]
    queue_list.append(deque(map(int, line.split())))

matrix = [0] * (number_of_columns * number_of_rows)
matrix_index = 0
queue_index = 0

# 处理矩阵填充
while matrix_index < len(matrix):  # 一直填充满窗口
    for _ in range(number_of_rows):  # 先按行填充
        if queue_list[queue_index]:
            matrix[matrix_index] = queue_list[queue_index].popleft()
            matrix_index += 1
            if matrix_index >= len(matrix):
                break
        else:
            break
    queue_index = (queue_index + 1) % len(queue_list)

# 按列优先顺序输出矩阵
for row in range(number_of_rows):
    for col in range(number_of_columns):
        print(matrix[col * number_of_rows + row], end=" ")