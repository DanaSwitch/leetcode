import sys


def solve():
    lines = sys.stdin.readline().strip().split()
    if not lines:
        return
    total_sum, n = int(lines[0]), int(lines[1])
    nums = list(map(int, sys.stdin.readline().strip().split()))

    # 小球总数没超过sum
    if sum(nums) <= total_sum:
        print("[]")
        return

    left, right = 0, max(nums)
    maxCapacity = 0
    while left <= right:
        mid = (left + right) // 2
        cur_sum = sum(min(mid, nums[i]) for i in range(n))
        if cur_sum <= total_sum:
            # 尝试增大mid
            maxCapacity = mid  # 更新
            left = mid + 1
        else:
            right = mid - 1
    result = [str(max(0, (nums[i] - maxCapacity))) for i in range(n)]
    print("["+ ",".join(result) +"]")

if __name__ == "__main__":
    solve()