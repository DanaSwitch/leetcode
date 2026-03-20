"""
输入	
5
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
2 computing  查询的层级和关键字
输出	2
说明	在第二层级上,computing出现了2次, 因此输出2
"""

from collections import defaultdict

# 读取日志条数
n = int(input())

# 二级字典：level_stats[层级][关键字] = 出现次数
"""
level_stats = {
    0: {"": 5, ...},                              # level 0(split 副产物)
    1: {"huawei": 4, ...},                        # level 1
    2: {"computing": 2, "cloud": 1, "wireless": 1}, # level 2
    3: {"no": 3},                                 # level 3
    4: {"one": 3},                                # level 4
}
"""
level_stats = defaultdict(lambda: defaultdict(int))

# 预处理: 遍历所有日志, 统计各层级关键字频次
for _ in range(n):
    # "/a/b/c".split("/") => ["", "a", "b", "c"]，索引即层级
    segments = input().split("/")
    for level, keyword in enumerate(segments):
        level_stats[level][keyword] += 1

# 读取查询条件
query = input().split()
target_level, target_keyword = int(query[0]), query[1]

# 查询对应层级上关键字的频次，不存在则返回 0
print(level_stats[target_level][target_keyword])