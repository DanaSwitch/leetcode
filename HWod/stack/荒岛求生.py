"""
5 10 8 -8 -5
输出: 2
说明: 第3个人和第4个人同归于尽, 第2个人杀死第5个人并剩余5战斗力, 第1个人没有遇到敌人。
"""
import sys

def solve():
    s = sys.stdin.readline().strip()
    if len(s) == 0:
        print(-1)
        sys.exit(0)
        
    ans = list(map(int, s.split()))
    
    # 检查是否有 0
    for num in ans:
        if num == 0:
            print(-1)
            sys.exit(0)

    # 栈结构处理碰撞
    stack = []
    for p in ans:
        alive = True
        # 只要当前向左走(p < 0)，且栈顶向右走(stack[-1] > 0)，就发生碰撞
        while alive and p < 0 and stack and stack[-1] > 0:
            right_power = stack[-1]
            left_power = abs(p)
            
            if right_power > left_power:
                # 栈顶（向右）赢了，扣除它消耗的体力，当前数字消失
                stack[-1] -= left_power
                alive = False
            elif right_power < left_power:
                # 当前数字（向左）赢了，削减它的绝对值，栈顶被撞碎，继续循环撞下一个
                p += right_power 
                stack.pop()
            else:
                # 同归于尽
                stack.pop()
                alive = False
       
        # 如果当前数字存活下来了，进栈
        if alive:
            stack.append(p)

    # 4. 栈里剩下的就是最终存活的人数
    print(len(stack))

if __name__ == "__main__":
    solve()