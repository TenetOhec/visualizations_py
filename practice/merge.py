def merge_sort(arr):
    """
    归并排序函数

    参数:
    arr (list): 待排序的列表
    """
    if len(arr) > 1:
        # 将列表分为两半
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 递归排序左右两半
        merge_sort(left_half)
        merge_sort(right_half)

        # 合并两个有序数组
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    """
    合并两个有序数组的函数

    参数:
    arr (list): 合并结果存放的列表
    left (list): 左半部分有序数组
    right (list): 右半部分有序数组
    """
    i = j = k = 0

    # 比较左右两个数组的元素，并按顺序合并到结果数组中
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 处理剩余的元素
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# 示例
my_list = [38, 27, 43, 3, 9, 82, 10]
print("原始列表:", my_list)

merge_sort(my_list)
print("排序后列表:", my_list)
