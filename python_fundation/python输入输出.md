# 输入输出处理

> 先读出输入
>
> 再map转化为对应的数据类型，如int



## input().strip().split()

`strip()` 的作用是**“去头去尾”**。

它会删除字符串**开头**和**结尾**的所有空白字符（包括空格、制表符 `\t`、换行符 `\n`）。

------

### 1. 为什么要加 `.strip()`？

> strip()首位切割，但是会保留空格，split()会以空格为分割符进行切割

虽然 `split()` 默认就会忽略空格，但在某些**极端或严谨**的场景下，加 `strip()` 是为了防止干扰：

- **处理换行符**：在某些在线评测系统（OJ）中，输入流的末尾可能带有看不见的 `\r\n`。虽然 `split()` 能处理，但 `strip()` 能确保你拿到的是干净的字符串。
- **防止空输入**：如果用户不小心多打了一个回车，或者输入行前后有大量空格，`strip()` 可以先把它清理干净。

### 2. 对比区别

假设输入内容是：`"  ABC  DEF  \n"` （前后都有空格，末尾有换行）

| **代码写法**              | **处理逻辑**                              | **结果**         |
| ------------------------- | ----------------------------------------- | ---------------- |
| `input().split()`         | 直接切分，忽略中间多余空格。              | `['ABC', 'DEF']` |
| `input().strip()`         | 先变成 `"ABC  DEF"`，去掉首尾空格和换行。 | `"ABC  DEF"`     |
| `input().strip().split()` | **先清空首尾**，再切分。                  | `['ABC', 'DEF']` |

### 3. 什么时候“必须”用 `strip()`？

如果你**不打算**使用 `split()`，而是想获取**一整行**输入（包括中间的空格），那么 `strip()` 就非常重要了。

**场景 A：获取带空格的句子**

Python

```
# 输入： "  I love Python  \n"
s = input().strip() 
# 结果： "I love Python" (去掉了两端空格，但保留了中间的)
```

**场景 B：读取单个字符或数字**

Python

```
# 输入： " 10 \n"
n = int(input().strip()) 
# 结果： 10 (如果不 strip，直接转换有时会受不可见字符干扰)
```



## sys.stdin.readline().strip()

- `sys.stdin.readline()` 每次只读**一行**。
- **坑点**：题目说 $M$ 最大有 100,000 个。在实际的测试数据中，这么长的数组**往往不会写在同一行里**，而是分成了很多行。
- **后果**：如果测试数据分行了，你的代码就只会读入第一行的那几个树，后面的树全丢了。程序会报错或者算出错误答案。

**修正建议**：永远建议使用 `sys.stdin.read().split()`，它可以一次性把所有行、所有空格隔开的数据全部读进来，不用担心换行符的问题。



## 重点： sys.stdin.read().split()

`sys.stdin.read().split()` 可以一次性把所有输入读进内存，处理速度极快，而且自动处理了换行符和空格，不需要一行行去 strip。

配合 `iter()` 使用，就像有一个指针，读一个就把指针往后移一位，非常优雅。

```python
raw_data = sys.stdin.read().split()  # 按 空格/换行符 将输入进行分开

if not raw_data:
    # 如果没有输入数据，直接结束
    sys.exit(0)

# 把所有字符串转换成整数，方便后面计算
# map(int, raw_data) 意思是对 raw_data 里的每一个元素都执行 int() 操作
data = list(map(int, raw_data))
```



### 前面某几个数，后面一堆数

```python
input_data = sys.stdin.read().split()

if not input_data:
    return

# 2. 创建一个迭代器，像指针一样方便我们需要时取下一个数据
iterator = iter(input_data)

# 依次取出 N, K, L
N = int(next(iterator))
K = int(next(iterator))
L = int(next(iterator))

# 接下来读取 N 个初始兵营人数
# 列表推导式配合迭代器，快速生成列表
camps = [int(next(iterator)) for _ in range(N)]
```



### 前面一堆数，后面几个数

```python
# 读取所有输入
data = sys.stdin.read().split()
if len(data) < 3: return

# 星号解包：nums 拿走前面所有，k 和 target 拿走最后两个
*nums_raw, k_raw, target_raw = data

# 转换类型并排序（排序是去重和双指针的前提）
nums = sorted(map(int, nums_raw))
k = int(k_raw)
target = int(target_raw)
```

