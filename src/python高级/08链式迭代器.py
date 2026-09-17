class ChainIterator:
    """
    把多个可迭代对象串联起来
    类似 itertools.chain 的简单实现
    """

    def __init__(self, *iterables):
        self.iterables = iter(iterables)    # 外层迭代器
        self.current = iter([])             # 当前正在遍历的迭代器

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self.current)   # 从当前迭代器取值
            except StopIteration:
                # 当前迭代器耗尽，切换到下一个
                self.current = iter(next(self.iterables))


# ---- 测试 ----
print("=== 链式迭代器 ===")

chain = ChainIterator([1, 2, 3], ['a', 'b', 'c'], (True, False))
print(list(chain))  # [1, 2, 3, 'a', 'b', 'c', True, False]

# Iterable（可迭代对象）
#     └── 实现 __iter__()
#
# Iterator（迭代器）⊂ Iterable
#     └── 实现 __iter__() + __next__()
#
# 所有迭代器都是可迭代对象
# 但可迭代对象不一定是迭代器