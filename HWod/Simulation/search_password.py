import sys

def main():
    words = sys.stdin.read().split()
    
    words.sort(key=lambda x: (len(x), x))  # 按长度和字典序升序

    valid = set()
    for w in words:
        # 长度为 1 的词直接合法, 或者去掉最后一个字符后的词已在合法集合中
        if len(w) == 1 or w[:-1] in valid:
            valid.add(w)

    if valid:
        result = sorted(valid, key=lambda x: (len(x), x))[-1]  # 取出最大的一个
        print(result)
    else:
        print("")

if __name__ == "__main__":
    main()