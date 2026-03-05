import heapq

# 1. 创建一个空堆
pq = []

# 2. 添加元素 (heappush)
heapq.heappush(pq, 10)
heapq.heappush(pq, 1)
heapq.heappush(pq, 5)

print(f"当前堆状态: {pq}") # 注意：内部是以数组存储的，并不完全有序，但 pq[0] 永远是最小的

# 3. 弹出最小值 (heappop)
smallest = heapq.heappop(pq)
print(f"弹出的最小值: {smallest}")
print(f"弹出后的堆: {pq}")

# 4. 将现有列表转化为堆 (heapify)
nums = [20, 3, 15, 7]
heapq.heapify(nums)
print(f"Heapify 后的列表: {nums}")