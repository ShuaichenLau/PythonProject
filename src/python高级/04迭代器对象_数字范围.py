class MyRange:
    """
    模拟 range() 的简单迭代器
    用法: MyRange(1, 6) 依次产出 1, 2, 3, 4, 5
    """

    def __init__(self, start, stop, step=1):
        self.current = start   # 当前值
        self.stop = stop       # 终止值
        self.step = step       # 步长

    def __iter__(self):
        # 返回迭代器本身（自身就是迭代器）
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration  # 没有更多元素，停止迭代
        value = self.current
        self.current += self.step
        return value


# ---- 测试 ----
print("=== MyRange 测试 ===")

# 方式1：for 循环（最常用）
for num in MyRange(1, 6):
    print(num, end=" ")   # 1 2 3 4 5
print()

# 方式2：手动调用 next()
r = MyRange(0, 4)
print(next(r))   # 0
print(next(r))   # 1
print(next(r))   # 2
print(next(r))   # 3
# print(next(r)) # 再调用会抛出 StopIteration

# 方式3：转成列表
print(list(MyRange(0, 10, 2)))  # [0, 2, 4, 6, 8]