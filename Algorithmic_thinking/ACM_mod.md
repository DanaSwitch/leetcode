# ACM模式下的输入输出

## 1.读入数组

```python
import sys
n = int(input().strip())
# input():标准输入读入一行字符串
# .strip():去掉字符串两端的空白字符(包括空格和换行符)
# int():将字符串转化为整形
nums = list(map(int, input().split()))
# map(函数, 可迭代对象) map将可迭代对象的每个元素以此应用到函数上, 并返回一个包含结果的新可迭代对象
# input().spilt() 对输入字符串进行分割
# list():将map对象转化为列表
```



> 输入：
>
> 5
>
> 1 2 3 4 5
>
> 输出：
>
> n = 5
>
> nums = [1, 2, 3, 4, 5]

## 2.读入字符串

```python
s = input().strip()
t = input().strip()
```

## 3.读入矩阵

```python
m, n = map(int, input().split())
matrix = [list(map.(int, input().split())) for _ in range(m)]
# for _ in range(m) 循环m次,等价于普通for循环

# 上面的一行代码等价于：
matrix = []
for i in range(n):  # 或者用 for _ in range(n)
    row = list(map(int, input().split()))
    matrix.append(row)
```



## 4.输入链表

```python
class ListNode:
    # 定义链表节点
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list(nums):
    # 根据输入数组创建链表
    if not nums:  # 空列表检查
        return None
    head = ListNode(nums[0])
    ptr = head
    for num in nums[1:]:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return head

def reverseList(head):
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

# 主程序部分
if __name__ == "__main__":
    # 读取输入并转换为整数列表
    nums = list(map(int, input().split()))
    
    # 构建链表
    head = linked_list(nums)
    
    # 反转链表
    new_head = reverseList(head)
    
    # 收集结果
    res = []
    while new_head:
        res.append(new_head.val)
        new_head = new_head.next
    
    # 输出结果
    print(res)
```



## 5.输入二叉树

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTravel(root):
    if not root:
        return []
    white, gray = 0, 1
    stack = [(root, white)]
    res = []
    while stack:
        node, color = stack.pop()
        if not node:
            continue
        if color == gray:
            res.append(node.val)
        else:
            stack.append((node.right, white))
            stack.append((node, gray))
            stack.append((node.left, white))
    return res

# 简单构建树的函数（这里简化为直接使用列表的第一个元素作为根）
def build_tree(nums):
    if not nums:
        return None
    # 这里简化为创建一个简单的树结构
    # 实际应用中，这里应该是根据nums构建完整二叉树
    root = TreeNode(int(nums[0]))
    if len(nums) > 1:
        root.left = TreeNode(int(nums[1]))
    if len(nums) > 2:
        root.right = TreeNode(int(nums[2]))
    return root

nums = input().split()
root = build_tree(nums)
res = inorderTravel(root)
print(res)
```

