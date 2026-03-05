import re

# 输入获取
str1 = input()
str2 = input()


# 算法入口
def getResult(str1, str2):
    pattern = r"[0-9a-f]+"  # +是尽可能得匹配

    valids = re.split(pattern, str1)  # 前一个剪刀, 后一个布料
    count = len(set(str2))  # 集合会自动去重
    # filter 过滤器
    ans = list(filter(lambda valid: valid != "" and len(set(valid)) <= count, valids))

    if len(ans) > 0:
        # 先按照
        ans.sort(key=lambda x: (-len(set(x)), [-ord(char) for char in x]))
        return ans[0]
    else:
        return "Not Found"


# 算法调用
print(getResult(str1, str2))