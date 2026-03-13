import sys
from collections import defaultdict

def solve():
    url_count = defaultdict(int)  # 记录每个URL被访问了多少次
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        if line.isdigit():
            n = int(line)
            # 访问次数多的排前面, 字典序小的排在前面
            # 字典有keys()方法, 会返回字典里面的所有键
            sorted_urls = sorted(url_count, key=lambda x: (-url_count[x], x))
            print(','.join(sorted_urls[:n]))
        else:
            url_count[line] += 1

solve()