import sys
from collections import defaultdict, deque

"""
 LFU缓存算法
 特点: 淘汰使用频率最低的元素, 如果频率相同，淘汰最久未使用的

 数据结构：
 1) keyMap: key -> [文件大小, 访问次数]
 2) freqMap: freq -> deque 存储 key, 左边为最久未使用, 右边为最近使用
"""

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity      # 总容量
        self.minFreq = 0          # 当前最小频率, 空时为 0
        self.useCap = 0           # 当前使用的容量
        self.keyMap = {}          # {文件:(文件大小, 访问次数)}
        self.freqMap = defaultdict(deque)  # {次数: 时间}
    # 模拟 get 操作: 访问一次 key, 就增加频率
    def get(self, key):
        # 如果 key 不存在，直接返回
        if key not in self.keyMap:
            return
        size, freq = self.keyMap[key]
        # 从原来频率的队列中删除该 key
        self.freqMap[freq].remove(key)
        # 如果该频率已经没有任何 key 了
        if not self.freqMap[freq]:
            del self.freqMap[freq]
            # 如果刚好是当前最小频率，则 minFreq +1
            if self.minFreq == freq:
                self.minFreq += 1
        # 频率 +1
        freq += 1
        self.keyMap[key][1] = freq
        # 加入新频率对应的队列末尾（表示最近访问）
        self.freqMap[freq].append(key)

    # 模拟 put 操作：插入新 key
    def put(self, key, value):
        # 如果 key 已经存在，则不处理
        if key in self.keyMap:
            return
        # 当容量不足时，需要进行淘汰
        while self.useCap + value > self.cap and self.useCap != 0 and self.minFreq != 0:
            # 找到最小频率对应的队列
            q = self.freqMap[self.minFreq]
            # 删除该队列中最久未使用的 key（队头）
            del_key = q.popleft()
            # 减掉该文件大小
            self.useCap -= self.keyMap[del_key][0]
            # 从 keyMap 删除
            del self.keyMap[del_key]
            # 如果当前频率队列被清空
            if not q:
                del self.freqMap[self.minFreq]
                # 重新计算 minFreq
                if self.freqMap:
                    self.minFreq = min(self.freqMap.keys())
                else:
                    self.minFreq = 0

        # 如果文件本身比总容量还大，直接返回
        if self.useCap + value > self.cap:
            return

        # 插入新文件，频率为 1
        self.keyMap[key] = [value, 1]
        self.freqMap[1].append(key)
        # 更新容量和最小频率
        self.useCap += value
        self.minFreq = 1

    # 获取所有文件名
    def getAllFile(self):
        return list(self.keyMap.keys())

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    idx = 0
    capacity = int(data[idx])  # 缓存最大值
    idx += 1
    n = int(data[idx])  # 文件操作个数
    idx += 1

    cache = LFUCache(capacity)

    for _ in range(n):
        cmd = data[idx]; idx += 1 
        if cmd == "put":  # 存储
            key = data[idx]; idx += 1  # 文件名
            value = int(data[idx]); idx += 1  # 文件大小
            cache.put(key, value)
        elif cmd == "get":
            key = data[idx]; idx += 1
            cache.get(key)

    files = cache.getAllFile()
    if not files:  # 如果没有文件，输出 NONE
        print("NONE")
        return
    files.sort()  # 按字典序排序
    print(",".join(files))

if __name__ == "__main__":
    main()
