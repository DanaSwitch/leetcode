import sys
import heapq

def solve():
    # 持续读取，直到 readline 返回空字符串（EOF）
    while True:
        line = sys.stdin.readline()
        if not line: break
        
        parts = line.split()
        if not parts: continue
        
        N, E = int(parts[0]), int(parts[1])  # 发动机个数, 手动启动发动机个数
        activation_time = [float('inf')] * N  # 初始化启动时间
        pq = []  # 记录所有起火事件
        
        for _ in range(E):
            t_p = sys.stdin.readline().split()
            if not t_p: continue
            t, p = int(t_p[0]), int(t_p[1])  # 手动起火时间, 位置
            if t < activation_time[p]:
                activation_time[p] = t  # 记下这个位置最早的起火时间
                heapq.heappush(pq, (t, p))  # 加入元组
        
        while pq:
            curr_t, curr_p = heapq.heappop(pq)  # 弹出最早的起火事件
            if curr_t > activation_time[curr_p]:
                continue
            # 左右扩散
            for neighbor in [(curr_p - 1) % N, (curr_p + 1) % N]:
                if curr_t + 1 < activation_time[neighbor]:
                    activation_time[neighbor] = curr_t + 1  # 更新起火时间
                    heapq.heappush(pq, (curr_t + 1, neighbor))  # 邻居起火加入队列
        
        max_t = max(activation_time)  # 记录最晚的起火时间
        # activation_time的下标就是发动机的序号
        res = [str(i) for i, t in enumerate(activation_time) if t == max_t]
        print(len(res))
        print(" ".join(res))  # join只接受字符串, 用str()改成字符串

if __name__ == "__main__":
    solve()