import sys

def parse_timestamp_to_milliseconds(time_str):
    """将时间戳字符串转换为毫秒数"""
    h, m, s, ms = map(int, time_str.replace('.', ':').split(':'))
    return ((h * 60 + m) * 60 + s) * 1000 + ms

def main():
    n = int(sys.stdin.readline().strip())  # 读取 n
    logs = [sys.stdin.readline().strip() for _ in range(n)]  # 读取日志列表

    # 使用稳定排序
    logs.sort(key=parse_timestamp_to_milliseconds)  # 自动调用parse_timestamp_to_milliseconds()处理每个对象

    # 输出排序后的日志
    sys.stdout.write("\n".join(logs) + "\n")  # join后面是胶水, 左右两边都粘起来

if __name__ == "__main__":
    main()