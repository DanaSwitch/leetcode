import sys

class App:
    """定义App类，封装App属性"""
    def __init__(self, name, priority, start_time, end_time):
        self.name = name
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time

def convert_time(time_str):
    """将 HH:MM 格式转换为分钟数（从00:00开始）"""
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def solve():
    # 1. 输入处理
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())

    all_apps = []  # 全局列表, 用来存放APP对象
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if len(parts) != 4:
            continue
        name = parts[0]
        priority = int(parts[1])
        start = convert_time(parts[2])
        end = convert_time(parts[3])
        all_apps.append(App(name, priority, start, end))

    query_str = sys.stdin.readline().strip()
    if not query_str:
        return
    query_time = convert_time(query_str)

    # 2. 记录已经注册的APP
    registered_apps = []

    for new_app in all_apps:
        # 起始时间必须小于结束时间，否则无法注册
        if new_app.start_time >= new_app.end_time:
            continue

        can_register = True
        to_unregister = []

        # 检查新App与已注册的所有App是否有冲突
        for reg in registered_apps:
            # 判断时间段重叠：max(start) < min(end)
            if max(new_app.start_time, reg.start_time) < min(new_app.end_time, reg.end_time):
                # 冲突发生：如果新App优先级更高，则记录待注销的App
                if new_app.priority > reg.priority:
                    to_unregister.append(reg)  # 将失败的App加入注销队列
                else:
                    # 优先级较低或相同，新App不能注册
                    can_register = False
                    break
        
        # 如果新App胜出，注销失败者并添加胜出的App
        if can_register:
            for item in to_unregister:
                registered_apps.remove(item)
            registered_apps.append(new_app)

    # 3. 结果查询
    result = "NA"
    for app in registered_apps:
        # 包含起始时间点，不包含结束时间点
        if app.start_time <= query_time < app.end_time:
            result = app.name
            break

    print(result)

if __name__ == "__main__":
    solve()