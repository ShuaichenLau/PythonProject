class Fibonacci:
    """
    无限斐波那契迭代器
    0, 1, 1, 2, 3, 5, 8, 13, 21 ...
    注意：无限迭代器必须配合 break 或 itertools.islice 使用
    """

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # 更新状态
        return value


# ---- 测试 ----
print("=== 斐波那契无限迭代器 ===")

fib = Fibonacci()

# 方式1：取前10个
result = []
for num in fib:
    result.append(num)
    if len(result) == 10:
        break
print("前10个:", result)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 方式2：配合 itertools.islice 更优雅
import itertools
fib2 = Fibonacci()
print("前10个:", list(itertools.islice(fib2, 10)))

# 方式3：找出100以内的斐波那契数
fib3 = Fibonacci()
print("100以内:", [n for n in itertools.takewhile(lambda x: x < 100, fib3)])