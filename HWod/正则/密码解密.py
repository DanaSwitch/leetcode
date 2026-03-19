import re

def main():
    input_str = input()

    # 正则替换优先选择替换 10* - 26*
    for i in range(26, 0, -1):
        regex_str = str(i)
        if i > 9:
            regex_str += r"\*"  # 转义 *
        replace_char = chr(ord('a') + i - 1)
        input_str = re.sub(regex_str, replace_char, input_str)

    print(input_str)

if __name__ == "__main__":
    main()
