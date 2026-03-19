import sys

def main():
    n = int(sys.stdin.readline().strip())  # 读取整数 n
    res = 0
    is_order = True
    count = 0

    for _ in range(2 * n):
        s = sys.stdin.readline().strip()  # 读取一行输入

        if "remove" in s:
            # 只在移除的时候进行调整
            if not is_order:
                res += 1
            is_order = True
            count -= 1
        elif "tail" in s:
            count += 1
        else:
            # 添加在头部会导致移除时乱序
            if count > 0:
                is_order = False
            count += 1

    print(res)

if __name__ == "__main__":
    main()