def binary_search(rates, target):
    """二分查找：在有序利率表中找 target，返回 (档位下标, 查找次数)；未找到返回 (-1, 查找次数)"""
    low, high = 0, len(rates) - 1
    count = 0  # 查找次数计数器

    # ---------- 循环：每次把查找区间缩小一半 ----------
    while low <= high:
        count += 1
        mid = (low + high) // 2      # 取中间档位
        if rates[mid] == target:     # 命中：返回档位
            return mid, count
        elif rates[mid] < target:    # 目标在右半区间，丢弃左半
            low = mid + 1
        else:                        # 目标在左半区间，丢弃右半
            high = mid - 1
    return -1, count                 # 未找到


def main():
    # 构造 1024 档模拟利率表：从 1.00% 起步，每档递增 0.01%
    rates = [round(1.00 + i * 0.01, 2) for i in range(1024)]
    target = 3.75

    index, count = binary_search(rates, target)
    if index != -1:
        print(f"找到 {target}%，位于档位下标 {index}（共 {len(rates)} 档）")
        print(f"查找次数：{count}")
    else:
        print(f"未找到 {target}%")


if __name__ == "__main__":
    main()
