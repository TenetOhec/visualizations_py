list_demo = [2, 5, 8, 4, 1, 9, 3, 7, 0, 6, -2]


class Mysort:
    def __init__(self, list_sort):
        self.list_sort = list_sort

    def __str__(self):
        return f"You want order list is {self.list_sort}"

    def bubble_sort(self):
        list_len = len(self.list_sort)
        for i in range(1, list_len):
            swapped = False
            for j in range(0, list_len - i):
                if self.list_sort[j] > self.list_sort[j + 1]:
                    swapped = True
                    temp = self.list_sort[j]
                    self.list_sort[j] = self.list_sort[j + 1]
                    self.list_sort[j + 1] = temp
            if not swapped:
                break
        return self.list_sort

    def select_sort(self):
        list_len = len(self.list_sort)
        for i in range(0, list_len - 1):
            min_index = i
            for j in range(i + 1, list_len):
                if self.list_sort[j] < self.list_sort[min_index]:
                    min_index = j
            if min_index != i:
                temp = self.list_sort[i]
                self.list_sort[i] = self.list_sort[min_index]
                self.list_sort[min_index] = temp
        return self.list_sort

    def insert_sort(self):
        list_len = len(self.list_sort)
        # 第一个元素有序，将后面n-1哥元素插入，有序序列，n-1轮
        for index in range(1, list_len):
            position = index
            current_value = self.list_sort[position]
            while position > 0 and self.list_sort[position - 1] > current_value:
                #将小于curren value 往后放
                self.list_sort[position] = self.list_sort[position - 1]
                position = position - 1
            # position 为 合适的插入位置
            self.list_sort[position] = current_value
        return self.list_sort
    """
    希尔排序：
    1:将数字分组
    2:给数组进行插入排序
    
    1:将数字分组
        子数组划分方法：
            以start为起点 相隔为gap-1个数
    """
    def shell_sort(self):

        gap = len(self.list_sort) // 2
        #直到gap = 1 进行最后一轮排序
        while gap > 0:
            for start_position in range(gap):
                self.gapInsertSort(start_position, gap)
                print("----")
                print(self.list_sort)
            gap = gap // 2
        return self.list_sort
    """
    2:给数组进行插入排序
        对子数组进行插入排序
    """
    def gapInsertSort(self, start, gap):
        for index in range(start+gap, len(self.list_sort), gap):
            current_value = self.list_sort[index]
            position = index
            while position >= gap and self.list_sort[position - gap] > current_value:
                self.list_sort[position] = self.list_sort[position - gap]
                position = position - gap
            self.list_sort[position] = current_value



obj = Mysort(list_demo)
print(str(obj))
# obj.bubble_sort()
# print(obj.bubble_sort())
print(obj.shell_sort())
