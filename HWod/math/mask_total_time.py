task_A, task_B, num = map(int, input().strip().split(','))

result = sorted(set(task_A*count + task_B*(num-count) for count in range(num+1)))

print("["+", ".join(map(str, result)) +"]")