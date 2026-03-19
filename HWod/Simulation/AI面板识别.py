import heapq

class Item:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __lt__(self, other):
        # 按 y 升序排序
        return self.y < other.y

def main():
    n = int(input())
    pq = []  # 使用 heapq 实现优先队列
    height = 0

    for _ in range(n):
        id, x1, y1, x2, y2 = map(int, input().split())
        heapq.heappush(pq, Item(id, x1, y1))
        height = (y2 - y1) * 0.5

    while pq:
        first = heapq.heappop(pq)
        # 当前行只有一个元素
        if not pq or pq[0].y - first.y > height:
            print(first.id, end=" ")
        else:
            ans = [first]

            # 迭代获取所有行的元素
            while pq and pq[0].y - first.y <= height:
                ans.append(heapq.heappop(pq))

            # 按 x 升序排序
            ans.sort(key=lambda item: item.x)

            for item in ans:
                print(item.id, end=" ")

if __name__ == "__main__":
    main()
