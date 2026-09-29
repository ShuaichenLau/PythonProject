class NumberList:
    """
    这是一个【可迭代对象】，不是迭代器
    区别：__iter__ 每次返回一个新的迭代器对象
    这样支持多次遍历！
    """

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # 每次调用都返回一个新的迭代器
        return NumberListIterator(self.data)


class NumberListIterator:
    """
    这是真正的【迭代器】
    """

    def __init__(self, data):
        self.data = data
        self.index = 0   # 记录当前位置

    def __iter__(self):
        return self  # 迭代器的 __iter__ 返回自身

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


# ---- 测试 ----
print("=== 可迭代对象 vs 迭代器 ===")

nums = NumberList([10, 20, 30, 40, 50])

# 可迭代对象可以多次遍历
print("第一次遍历:", list(nums))   # [10, 20, 30, 40, 50]
print("第二次遍历:", list(nums))   # [10, 20, 30, 40, 50]  不会为空

# 迭代器只能遍历一次
iterator = iter(nums)   # 获取迭代器
print("迭代器第一次:", list(iterator))  # [10, 20, 30, 40, 50]
print("迭代器第二次:", list(iterator))  # []   已经耗尽