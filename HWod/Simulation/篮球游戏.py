"""
思路: 对出队的每个元素, 在入队的队伍里找
"""
from collections import deque

def solve():
    input_balls = list(map(int, input().strip().split(',')))
    output_balls = list(map(int, input().strip().split(',')))
    
    # 检查所有要取出的篮球是否存在于放入序列中
    input_set = set(input_balls)
    for b in output_balls:
        if b not in input_set:
            print("NO")
            return
    
    queue = deque()
    input_idx = 0
    result = []
    
    for ball in output_balls:
        # 如果目标篮球不在队列中, 继续放入篮球直到放入目标篮球
        if ball not in queue:
            while input_idx < len(input_balls):
                queue.append(input_balls[input_idx])
                input_idx += 1
                if input_balls[input_idx - 1] == ball:
                    break
            else:
                print("NO")
                return
        
        # 判断目标篮球在左端还是右端
        if len(queue) == 1:
            # 只剩一个，必须从左边取
            queue.popleft()
            result.append('L')
        elif queue[0] == ball:
            queue.popleft()
            result.append('L')
        elif queue[-1] == ball:
            queue.pop()
            result.append('R')
        else:
            # 篮球在中间，无法取出
            print("NO")
            return
    
    print(''.join(result))

solve()