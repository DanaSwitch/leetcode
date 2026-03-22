import sys
import math

def parse_time(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def effective_minutes(begin, end):
    free_start, free_end = 11 * 60 + 30, 13 * 60 + 30
    duration = max(0, end - begin)
    overlap = max(0, min(end, free_end) - max(begin, free_start))
    return duration - overlap

n = int(sys.stdin.readline().strip())
monthly_cards = set()
for _ in range(n):
    monthly_cards.add(sys.stdin.readline().strip())

records = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    time_str, plate, action = line.split()
    if plate in monthly_cards:
        continue
    records.setdefault(plate, []).append((parse_time(time_str), action))

total_fee = 0
for logs in records.values():
    logs.sort()
    fee = 0
    stack = []
    for t, d in logs:
        if d == 'enter':
            stack.append(t)
        elif d == 'leave' and stack:
            minutes = effective_minutes(stack.pop(), t)
            if minutes >= 30:
                fee += math.ceil(minutes / 30)
                if fee >= 15:     # ✅ 单车封顶，立即break
                    fee = 15
                    break
    total_fee += fee

print(total_fee)