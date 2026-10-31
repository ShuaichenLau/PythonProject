import time
from multiprocessing import Process


def eat():
    for i in range(10):
        print(f'正在吃饭 == {i}')
        time.sleep(0.1)


def work():
    for i in range(10):
        print(f'正在工作 == {i}')
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建一个紫禁城 每个任务由独立的紫禁城来完成
    p1 = Process(target=eat,name='进程1')
    p2 = Process(target=work,name='进程2')
    p1.start()
    p2.start()


# 这个代码中 Process(target=eat,name='进程1') 这里eat不用加括号, 但这是方法名. 我应该区分变量名和方法名?
# # Python 中函数名不加括号的本质
#
# ## 核心概念：函数是"一等公民"
#
# 在 Python 中，**函数本身也是一个对象**，函数名就是指向这个对象的**变量（引用）**。
#
# ```python
# def eat():
#     print("正在吃饭")
#
# # 加括号   —— 立刻【调用执行】函数，返回函数的返回值
# eat()        # 执行函数，输出"正在吃饭"，返回 None
#
# # 不加括号 —— 【引用】这个函数对象本身，不执行
# eat          # 就是函数对象本身，类似 <function eat at 0x...>
#
# print(type(eat))    # <class 'function'>   它就是个对象
# print(type(eat()))  # <class 'NoneType'>   调用后拿到返回值的类型
# ```
#
# ---
#
# ## 直接对比
#
# ```python
# def eat():
#     print("正在吃饭")
#
# # ✅ 传函数引用 —— 把"函数对象"交给 Process，让它在新进程里调用
# p1 = Process(target=eat)    # 正确：传的是函数本身
#                              # Process 内部会在新进程里执行 eat()
#
# # ❌ 传函数返回值 —— 立刻执行了 eat()，把返回值(None)传给 Process
# p2 = Process(target=eat())  # 错误：eat() 已经在主进程执行完了
#                              # target=None，新进程啥也不干
# ```
#
# ---
#
# ## 用变量类比，一下就懂
#
# ```python
# # 整数变量
# x = 10
# print(x)    # 10        —— 取出变量的值
# print(x+1)  # 11        —— 对变量的值进行操作
#
# # 函数变量（完全一样的逻辑！）
# def eat():
#     print("吃饭")
#
# f = eat          # f 和 eat 指向同一个函数对象（就是个赋值）
# f()              # 调用它，输出"吃饭"
# print(f == eat)  # True，指向同一个对象
#
# # 所以 Process(target=eat) 本质上就是：
# # 把 eat 这个变量（函数对象）赋值给 target 参数
# # Process 拿到之后，在新进程里自己去调用它
# ```
#
# ---
#
# ## 更多常见的"传函数引用"场景
#
# ```python
# # ---- 1. 排序 ----
# students = [('Tom', 88), ('Jerry', 95), ('Bob', 72)]
#
# # 传函数引用给 key，sorted 内部自己去调用
# students.sort(key=lambda x: x[1])      # ✅ lambda 也是函数对象
# students.sort(key=str.lower)           # ✅ 方法也是函数对象
#
# # ---- 2. map / filter ----
# nums = [1, 2, 3, 4, 5]
# result = list(map(str, nums))          # ✅ 传 str 函数引用
# evens  = list(filter(lambda x: x % 2 == 0, nums))  # ✅
#
# # ---- 3. 回调函数 ----
# def on_click():
#     print("按钮被点击了")
#
# # button.command = on_click   # ✅ Tkinter 等 GUI 框架的回调
# # button.command = on_click() # ❌ 立刻执行，拿到 None 注册进去
#
# # ---- 4. 多进程/多线程 ----
# from multiprocessing import Process
# from threading import Thread
#
# Process(target=eat)   # ✅ 传引用，新进程里调用
# Thread(target=eat)    # ✅ 传引用，新线程里调用
# ```
#
# ---
#
# ## 一张图总结
#
# ```
# 函数名（不加括号）          函数调用（加括号）
# ─────────────────          ─────────────────
# eat                         eat()
#   │                           │
#   │ 是一个【函数对象】          │ 立即执行，返回【函数的返回值】
#   │ 可以赋值、传参、存储        │ 这里返回 None
#   ↓                           ↓
# 可以传给别人，                已经执行完了，
# 让别人决定什么时候调用          别人拿到的只是 None
# （Process、Thread、map...）
# ```
#
# > 💡 **一句话记住：**
# > - **有括号** = 我现在就要执行它，给你**结果**
# > - **没括号** = 我把它**本身**交给你，你决定什么时候执行