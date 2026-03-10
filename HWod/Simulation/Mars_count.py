"""
思路: 先找到优先级更高的 # 将左右的group(1)和group(2)进行计算后, 用replace(data.group(),str(),1)
      进行替换, 反复进行
      最后split('$')进行切割, 从左至右进行计算
"""
import re

if __name__ == "__main__":
    data = input()

    while True:
        # 注意是反斜杠\
        part = re.search(r'(\d+)#(\d+)', data)  # 打包
        if not part:
            break
        # group 是识别括号里面的内容
        a, b = int(part.group(1)), int(part.group(2))
        # replace 只能替换字符串
        data = data.replace(part.group(), str(4*a + 3*b + 2), 1)
    
    # 切割 $
    nums = list(map(int, data.split('$')))
    result = nums[0]
    for i in nums[1:]:    
        result = 2*result + i + 3
    
    print(result)