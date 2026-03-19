"""
输入
10 6 3
-1 1 2 3 100 10 13 9 10
输出
8
说明
S[0], S[4] S[7], S[8]为错误值。S[0]之前没有正常的采样数据, 丢弃S[0]。
S[4]和S[7]不满足故障条件, 此值分别由S[3]和S[6]代替, 即S[4]为3, S[7]为13。
替换后, S[8]小于S[7]，也是错误值。
"""
import sys
from collections import deque

def valid(v, last):
    """判断采样值 v 是否为正常值"""
    if v < 0: 
        return False  # 负数为错误值
    if last is not None and (v < last or v - last >= 10): 
        return False  # 比上一正常值小，或差值>=10，为错误值
    return True

def main():
    m, t, p = map(int, sys.stdin.readline().split())
    # m: 故障检测窗口大小, t: 窗口内错误次数触发故障, p: 恢复所需连续正常周期数
    seq = list(map(int, sys.stdin.readline().split()))

    last = None        # 最近一个正常值, None 表示尚无正常值
    cur = max_len = 0  # cur: 当前连续正常周期数, max_len: 历史最大值
    win = deque()      # 滑动窗口, 存储最近 m 个周期内错误值的索引

    i = 0
    while i < len(seq):
        # 清除已滑出窗口的旧错误索引（超过 m 个周期前的）
        while win and win[0] <= i - m:
            win.popleft()

        if valid(seq[i], last):
            # ── 正常值：更新 last，累加连续长度 ──
            last = seq[i]
            cur += 1
            max_len = max(max_len, cur)
        else:
            # ── 错误值：记录到滑动窗口 ──
            win.append(i)

            if len(win) < t:
                # 窗口内错误数未达到阈值，尚未触发故障
                if last is not None:
                    # 有历史正常值：用 last 替换错误值，仍计入连续周期
                    cur += 1
                    max_len = max(max_len, cur)
                # 无历史正常值：直接丢弃，cur 不增加
            else:
                # 窗口内错误数达到阈值 t，触发故障
                # 向后扫描，寻找 p 个连续正常值作为恢复条件
                j, pcount, rec_last = i + 1, 0, None
                while j < len(seq) and pcount < p:
                    if valid(seq[j], rec_last):
                        # 当前恢复阶段的正常值，连续计数+1
                        rec_last = seq[j]
                        pcount += 1
                    else:
                        # 恢复期间出现错误, 连续计数归零重来
                        pcount, rec_last = 0, None
                    j += 1
                # 故障期间（含恢复阶段）数据全部丢弃，重置所有状态
                cur, last = 0, None
                win.clear()
                i = j - 1  # 外层 i+=1 后恰好从恢复点之后继续
        i += 1
    print(max_len)

if __name__ == "__main__":
    main()