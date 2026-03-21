"""
5 10 8 -8 -5
输出: 2
说明: 第3个人和第4个人同归于尽, 第2个人杀死第5个人并剩余5战斗力, 第1个人没有遇到敌人。
这题使用栈, 因为最后大于0的数要先和第一个小于0的数字进行碰撞, 后进先出
"""
line = input().strip()
# 输入异常
if not line:
    print(-1)
    exit()
parts = list(map(int, line.split()))
n = len(parts)

# 输入异常
if n == 0 or n > 30000:
    print(-1)
    exit()
stack = []

for num in parts:
    # 输入异常
    if num == 0:
        print(-1)
        exit()
    # 向右 直接入栈
    if num > 0:
        stack.append(num)
    else:
        # 向左需要考虑碰撞情况
        power = num
        while stack and stack[-1] > 0 and power != 0:
            top = stack.pop()
            # 消耗栈顶体力
            if top > abs(power):
                stack.append(top - abs(power))
                power = 0
            # 两者抵消
            elif top == abs(power):
                power = 0
            else:  # 没打过, 继续下一轮
                power += top
        if power != 0:
            stack.append(power)
# 栈中元素数量就是答案
print(len(stack))