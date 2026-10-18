"""排序基准测试：冒泡排序（自实现） vs 合并排序（Step1 的 merge_sort）"""
import random
import timeit

from merge_sort import merge_sort


def bubble_sort(nums):
    """冒泡排序（自实现）：相邻元素两两比较，每趟把当前最大值"冒泡"到末尾"""
    a = nums[:]                      # 拷贝一份，保证不改原数组、每次计时都是对同一原始数据排序
    n = len(a)
    for i in range(n - 1):           # 最多 n-1 趟
        swapped = False
        for j in range(n - 1 - i):   # 每趟比较相邻元素
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:              # 本趟无交换说明已有序，提前结束
            break
    return a


def bench(func, arr, repeat=3):
    """用 timeit 对同一数组计时：number=1 跑一遍算一次，共 repeat=3 次，返回平均耗时"""
    runs = timeit.repeat(lambda: func(arr), number=1, repeat=repeat)
    return sum(runs) / len(runs)


def main():
    random.seed(42)  # 固定随机种子，结果可复现
    print(f"{'n':>6} | {'冒泡耗时(s)':>12} | {'合并耗时(s)':>12} | {'倍数':>8}")
    print("-" * 50)
    for n in (1000, 2000, 4000, 8000):
        arr = [random.randint(0, 10**6) for _ in range(n)]  # 每档生成随机数组一份
        t_bubble = bench(bubble_sort, arr)
        t_merge = bench(merge_sort, arr)
        print(f"{n:>6} | {t_bubble:>12.4f} | {t_merge:>12.4f} | {t_bubble / t_merge:>7.1f}x")


if __name__ == "__main__":
    main()
