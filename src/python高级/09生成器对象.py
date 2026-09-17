def my_generator():
    print("--- 步骤 1 ---")
    yield "A"
    print("--- 步骤 2 ---")
    yield "B"
    print("--- 步骤 3 ---")
    yield "C"

# 1. 调用函数，此时内部代码完全没有执行，仅返回一个生成器对象
gen = my_generator()
print(type(gen))  # 输出: <class 'generator'>

# 2. 通过 next() 触发执行，直到遇到 yield 暂停
print(next(gen))
# 输出:
# --- 步骤 1 ---
# A

print(next(gen))
# 输出:
# --- 步骤 2 ---
# B

# 3. 也可以直接用 for 循环消费剩余的元素
for val in gen:
    print(val)
# 输出:
# --- 步骤 3 ---
# C


print('==============================================')
# 列表推导式：立刻计算出所有值，占用大量内存
list_comp = [x * 2 for x in range(5)]
print(list_comp)  # 输出: [0, 2, 4, 6, 8]

# 生成器表达式：不立刻计算，只在需要时生成
gen_exp = (x * 2 for x in range(5))
print(gen_exp)    # 输出: <generator object <genexpr> at 0x...>

# 获取值
print(next(gen_exp))  # 输出: 0
print(next(gen_exp))  # 输出: 2
print(next(gen_exp))  # 输出: 4
print(next(gen_exp))  # 输出: 6
print(next(gen_exp))  # 输出: 8

# print(next(gen_exp))  # 输出: Traceback (most recent call last):
# Traceback (most recent call last):
#   File "C:\Users\Lenovo\PycharmProjects\PythonProject\src\python高级\09生成器对象.py", line 48, in <module>
#     print(next(gen_exp))  # 输出: 10
#           ~~~~^^^^^^^^^
# StopIteration