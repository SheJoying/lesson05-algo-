def merge_sort(nums):
    """合并排序（分治法）：严格按「分解 - 解决 - 合并」三段结构实现"""
    # ---------- 递归出口：子数组长度 <= 1 时天然有序 ----------
    if len(nums) <= 1:
        return nums

    # ========== 1. 分解 ==========
    # 从中间位置把数组一分为二，形成两个规模更小的子问题
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    # ========== 2. 解决 ==========
    # 递归地对左右两半分别排序（子问题结构与原问题相同）
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # ========== 3. 合并 ==========
    # 将两个已排好序的子数组合并成一个整体有序的数组
    merged = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
    # 某一侧扫描完后，把另一侧剩余元素直接接到结果末尾
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])
    return merged


def main():
    nums = [8, 3, 5, 1, 9, 2]
    print(merge_sort(nums))


if __name__ == "__main__":
    main()
