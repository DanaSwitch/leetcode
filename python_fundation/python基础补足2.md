## continue和break

continue 是跳过本次循环，if后面的代码都不执行，开启下一次循环

```python
for L in range(max_val, total_sum + 1):
    if total_sum % L != 0:
        continue
```



break就是直接结束这个循环

```python
# 尝试连接现有顺子
for sequence in grouped:
    if rank_map[current_card] - rank_map[sequence[-1]] == 1:  # 新牌比最后一个牌大1
        sequence.append(current_card)  # 在当前列表添加
        is_extended = True
        break
```



**`return`**：彻底结束整个函数（最干脆利落）





## sorted()排序

nums = sorted(list(map(int, input().split())))





### 字典的三个方法

| **方法**        | **返回内容**         | **例子**                          |
| --------------- | -------------------- | --------------------------------- |
| **`.keys()`**   | 所有的键（ID）       | `[1, 5]`                          |
| **`.values()`** | 所有的值（数据列表） | `[[200, 90], [5, 80]]`            |
| **`.items()`**  | **所有的键 + 值**    | `[(1, [200, 90]), (5, [50, 80])]` |



同时取出字典的键和值：

```python
for item_id, info in low_price_map.items():
    total_qty, original_price = info
    final_price = original_price
```





### append 和 pop

遵循”后进先出“的原则：

> append(gem[i]) 是将元素放在列表的最后面，selected.pop() 是将最后一个元素弹出来