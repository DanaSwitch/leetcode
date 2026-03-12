import sys

# 将时间转换为分钟
def parse_time(t):
    h, m = map(int, t.split(":"))
    return h*60 + m

# 计算每次进入的有效停车时间
def cost(begin, end):
    free_start, free_end = 11*60+30, 13*60+30  # 免费时段
    duration = max(0, end-begin)
    # 取出交集 max(开始) < min(结束): 有交集
    overlap_start = max(begin, free_start)
    overlap_end = min(end, free_end)
    if overlap_start < overlap_end:
        duration -= (overlap_end - overlap_start)
    return duration

# 读入包月车辆数量
n_line = sys.stdin.readline().strip()
n = int(n_line)

monthly_cards = set()
for _ in range(n):
    card = sys.stdin.readline().strip()
    monthly_cards.add(card)

# 读入出入记录
records = {}
for line in sys.stdin:  # 一直读, 至到手动结束
    line = line.strip()
    if not line:
        continue
    time, card, state = line.split()
    if card in monthly_cards:
        continue
    time_minute = parse_time(time)
    records.setdefault(card, []).append((time_minute, state))  # {车牌: (时间, 状态)}

total_cost = 0
for log in records.values():  # 处理单量车的所有记录
    log.sort()  # 按时间升序
    fee = 0
    stack = []
    for time, state in log:
        if state == 'enter':
            stack.append(time)
        elif state == 'leave' and stack:
            in_time = stack.pop()
            out_time = time
            duration = cost(in_time, out_time)
            if duration >= 30:  # 不足30不计费
                charge = (duration + 29)//30
                fee += charge
                if fee >= 15:
                    fee = 15
                    break
    total_cost += fee

print(total_cost)