## 个人总结

```python
dp = [n] * (target + 1)  # dp[j] 表示要达到重量 j 至少需要多少石头
```

n 表示总共n个石头, 意思是不可能达到

target + 1表示target + 1个dp数组，我们要算的是索引为target，目标为target的dp[target]

定义为 `target + 1` 后，数组的索引和物理意义就完全同步了：

- `dp[0]`：对应重量为 0。
- `dp[1]`：对应重量为 1。
- ...
- `dp[target]`：对应重量为 `target`。

这种“空间换直觉”的做法，可以让你在写代码时不需要在大脑里进行 `重量 - 1` 的换算，极大地降低了出错的概率。





def函数不是定义在class下面的话，不用定义self

readline() 记得加()

/ 是得到浮点数，//才会得到整数

if __name__ == "__main__":       只有main有“”

题目要求打印“-1”的要print(-1)，return -1 是直接返回了

