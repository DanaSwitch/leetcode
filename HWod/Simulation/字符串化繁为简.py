import sys

def solve():
    input_string = sys.stdin.readline().strip()
    if not input_string:
        print("0")
        return

    # 只把真正在括号里出现的字符加入并查集
    insides = set()
    insides_groups = []  # 括号内的字母
    
    # 1. 提取括号内的数据
    i = 0
    while i < len(input_string):
        if input_string[i] == '(':
            j = input_string.find(')', i)  # 找不到会返回-1
            if j != -1:
                group = input_string[i+1 : j]
                valid_chars = [c for c in group if c.isalpha()]
                if valid_chars:
                    insides_groups.append(valid_chars)
                    insides.update(valid_chars)  # update 批量更新集合
                i = j + 1
            else:
                i += 1
        else:
            i += 1

    # 2. 初始化字典版并查集 (老大默认是自己)
    parent = {c: c for c in insides}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 路径压缩
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            # 核心：永远让 ASCII 码更小的字符当老大 (如 'A' < 'a')
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y

    # 3. 合并同一个括号内的字符
    for group in insides_groups:
        for k in range(1, len(group)):
            union(group[0], group[k])

    # 4. 搭建“大小写等效”的桥梁 (模仿 V2 的核心逻辑)
    # 如果大写和小写都真真实实地出现在了括号里(不论是否同组)，将它们合并
    for lower_c in 'abcdefghijklmnopqrstuvwxyz':
        upper_c = lower_c.upper()
        if lower_c in parent and upper_c in parent:
            union(lower_c, upper_c)

    # 5. 生成输出结果
    res = []
    inside_parentheses = False  # 内外隔离
    
    for c in input_string:
        if c == '(':
            inside_parentheses = True
        elif c == ')':
            inside_parentheses = False
        else:
            # 确保访问的是()外面的字母, 不改变大小写
            if not inside_parentheses:
                # 核心替换逻辑：如果这个字符精确存在于并查集里，就换成它的老大
                if c in parent:
                    res.append(find(c))
                else:
                    res.append(c) # 不在括号里出现过的，原样保留！

    final_str = "".join(res)
    print(final_str if final_str else "0")

if __name__ == "__main__":
    solve()