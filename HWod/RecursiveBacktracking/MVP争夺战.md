

```python
seen = set()  # 避免重复尝试相同的桶（剪枝优化）
for i in range(k):
    if buckets[i] in seen:
        continue
        if buckets[i] + scores[idx] <= target:  # 放得下才尝试
            seen.add(buckets[i])
            buckets[i] += scores[idx]
            if backtrack(idx + 1):  # 后续递归能成功
                return True
            buckets[i] -= scores[idx]  # 回退, 尝试其他方案

            return False  # 所有桶都试过，没有可行方案
```



### 问题：

            if buckets[i] + scores[idx] <= target:  # 放得下才尝试
                seen.add(buckets[i])
那这个不是成功了添加的吗，不应该是失败了添加吗



### 回答：

每一层的递归都有一个独立的seen

这里的 `seen` 记录的不是“结果”，而是**“我这一轮已经做过的尝试”**。

想象你面前有 3 个一模一样的空箱子（A, B, C），你手里有一个 5 分的球：

1. **看箱子 A**：它是 0 分。`0` 不在 `seen` 里。
2. **做记录**：立刻把 `0` 加入 `seen`。这代表：**“在这一层递归里，我已经尝试过把球放进一个‘当前积分为 0’的箱子里了。”**
3. **去尝试**：把球放进 A，看看后面能不能成功。
4. **看箱子 B**：它是 0 分。代码检查 `if 0 in seen`——**命中！**
5. **跳过**：因为箱子 B 和 A 是一样的，既然你已经试过“把球放进一个 0 分箱子”了，就没必要在同一个递归层级里再试一次。