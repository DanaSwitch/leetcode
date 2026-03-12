# 输入获取
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

# 算法入口
def solve():
    message = []
    for i in range(0, len(line1), 2):
        message.append([line1[i], line1[i + 1]])  # (时间, 内容)
    consumer = []
    for i in range(0, len(line2), 2):
        consumer.append([line2[i], line2[i + 1]])  # (开始时间, 结束时间)

    message.sort(key=lambda x: x[0])  # 按时间升序
    result = [[] for _ in range(len(consumer))]  # 嵌套列表

    # 遍历消息
    for time, content in message:
        # 倒序遍历订阅者, 因为后面的订阅者优先级更高, 因此倒序可以实现高优先级的订阅者先匹配到发布者
        for j in range(len(consumer) - 1, -1, -1):
            start, end = consumer[j]
            # 如果 订阅时刻 <= 发布时刻 < 取消订阅时刻
            if end > time >= start:
                result[j].append(content)  # 加入内容
                break  # 结束内层循环, 确保这条消息不会被别人拿到

    for contents in result:
        if len(contents) == 0:
            print("-1")
        else:
            print(" ".join(map(str, contents)))

# 算法调用
solve()