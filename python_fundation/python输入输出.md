# 输入输出处理

> 先读出输入
>
> 再map转化为对应的数据类型，如int

## sys.stdin.readline.strip()

- `sys.stdin.readline()` 每次只读**一行**。
- **坑点**：题目说 $M$ 最大有 100,000 个。在实际的测试数据中，这么长的数组**往往不会写在同一行里**，而是分成了很多行。
- **后果**：如果测试数据分行了，你的代码就只会读入第一行的那几个树，后面的树全丢了。程序会报错或者算出错误答案。

**修正建议**：永远建议使用 `sys.stdin.read().split()`，它可以一次性把所有行、所有空格隔开的数据全部读进来，不用担心换行符的问题。



## sys.stdin.read.strip()

```python
raw_data = sys.stdin.read().split()  # 按 空格/换行符 将输入进行分开

if not raw_data:
    # 如果没有输入数据，直接结束
    sys.exit(0)

# 把所有字符串转换成整数，方便后面计算
# map(int, raw_data) 意思是对 raw_data 里的每一个元素都执行 int() 操作
data = list(map(int, raw_data))
```

