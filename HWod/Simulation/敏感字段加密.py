import sys

index = int(sys.stdin.readline().strip())
command_strs = sys.stdin.readline().strip()

command_list = []  # 存储命令
cur_command = ""  # 当前命令
in_quotes = False  # 是否在双引号内

for i, char in enumerate(command_strs):
    if char == '"':
            cur_command += char
            if not in_quotes:  # 第一个"
                in_quotes = True
            else:              # 第二个", 结束当前命令
                command_list.append(cur_command)
                cur_command = ""  # 重置
                in_quotes = False
    elif not in_quotes and char == '_':  # ""外的下划线, 拆分命令
        if cur_command:
            command_list.append(cur_command)
            cur_command = ""
    elif i == len(command_strs) - 1:  # 处理最后一个字符
        cur_command += char
        command_list.append(cur_command)
        cur_command = ""
    else:
        cur_command += char

# 检查索引合法性
if index < 0 or index >= len(command_list):
    print("ERROR")
else:
    command_list[index] = "******"  # 替换指定索引
    print("_".join(command_list))  # 连接成最终结果