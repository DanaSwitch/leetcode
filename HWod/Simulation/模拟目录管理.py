import sys

def is_valid_dirname(name):
    """
    判断目录名称是否合法：
    1. 特殊目录 ".." 是合法的
    2. 仅支持小写字母
    3. 限制10个字符以内
    4. 不支持嵌套和绝对路径(即不能包含 '/')
    """
    if name == "..":
        return True
    
    # 检查长度和非法字符 (isalpha()保证全是字母, islower()保证全是小写)
    if len(name) > 10 or not name.isalpha() or not name.islower():
        return False
        
    return True

def main():
    # file_system 代表根目录 '/'
    # 字典的键是目录名, 值是子目录（也是字典）
    file_system = {} 
    
    # current_path 记录当前路径层级, 空列表代表在根目录
    current_path = [] 
    
    # 记录最后一条有效命令的输出结果
    last_output = "" 

    # 逐行读取输入
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        cmd = parts[0]

        # 每次执行命令前，先根据 current_path 找到当前所在的目录字典
        current_dir = file_system
        for folder in current_path:
            current_dir = current_dir[folder]

        # 处理 mkdir 命令
        if cmd == "mkdir" and len(parts) == 2:
            dirname = parts[1]
            if is_valid_dirname(dirname) and dirname != "..":
                # 如果目录不存在，则创建（在字典中新增一个空字典）
                if dirname not in current_dir:
                    current_dir[dirname] = {}
            # mkdir 无输出，清空上一次的结果
            last_output = "" 

        # 处理 cd 命令
        elif cmd == "cd" and len(parts) == 2:
            dirname = parts[1]
            if is_valid_dirname(dirname):
                if dirname == "..":
                    # 返回上一级，只需要把路径列表的最后一个元素弹出
                    if current_path: # 前提是当前不在根目录
                        current_path.pop()
                else:
                    # 进入子目录，前提是该目录存在
                    if dirname in current_dir:
                        current_path.append(dirname)
            # cd 无输出，清空上一次的结果
            last_output = "" 

        # 处理 pwd 命令
        elif cmd == "pwd" and len(parts) == 1:
            if not current_path:
                last_output = "/"
            else:
                # 把列表拼接成路径字符串，并在头尾加上 '/'
                last_output = "/" + "/".join(current_path) + "/"

        # 无效命令不做任何处理，且没有输出（在我们的逻辑里会自动被忽略）

    # 题目要求输出最后一条命令运行结果
    if last_output:
        print(last_output)

if __name__ == "__main__":
    main()