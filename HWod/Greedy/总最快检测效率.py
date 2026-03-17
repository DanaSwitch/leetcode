lines = list(map(int, input().split()))
m, n = lines[0], lines[1]  # 采样员人数, 志愿者人数
nums = list(map(int, input().split()))  # 基准值
base_total = 0  # 没有志愿者的效率
v_nums = []  # 添加志愿者

for i in range(m):
    M = nums[i] // 10
    base_total += nums[i] - 2*M
    v_nums.append(2*M)  # 一个之原则和
    v_nums.append(M)
    v_nums.append(M)
    v_nums.append(M)

v_nums.sort(reverse=True)  # 从大到小

print(base_total+sum(v_nums[:n]))