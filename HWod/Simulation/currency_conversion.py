"""
思路: 用rate{} 字典记录汇率, re.findall()提取数字和货币, 然后转换累加
"""
import re

def main():
    # 汇率映射表：每个单位对应 1 单位该货币是多少“人民币分”
    rates = {
        "CNY": 100, "fen": 1,
        "HKD": 10000 / 123, "cents": 100 / 123,
        "JPY": 10000 / 1825, "sen": 100 / 1825,
        "EUR": 10000 / 14, "eurocents": 100 / 14,
        "GBP": 10000 / 12, "pence": 100 / 12
    }

    n = int(input())
    total_fen = 0
    
    for _ in range(n):
        record = input().strip()
        # 使用正则表达式提取 (数字, 单位) 对
        parts = re.findall(r'(\d+)([a-zA-Z]+)', record)  # findall()找到返回
        for amount, unit in parts:
            if unit in rates:
                total_fen += int(amount) * rates[unit]
    
    print(int(total_fen))

if __name__ == "__main__":
    main()