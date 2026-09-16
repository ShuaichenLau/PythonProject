'''
遍历字符串
'''
from functools import reduce

str1 = 'asdfghjkl'

# for tiem in str:
#     print(tiem)


lst = ['11', 1, True]
print(f'集合长度是{len(lst)}')
print(lst)

# list集合可以存放不同类型的数据,是可变数组


list2 = [1, 2, 'he,aa', ['11', '22'], 'aa']
print(list2)
print('=============================')

#  i是下标  e是元素 enumerate是枚举
for i, e in enumerate(list2):
    print(i, e)

print('=======================倒序输出=====')
print(list2[::-1])

print(type(list2))

print('=======================元祖=====')
# 元祖  不可变数组
t1 = ()
t2 = tuple()

print(type(t1))
print(type(t2))

t3 = (1, 2, 'he,aa', ['11', '22'], 'aa')
print(f't3 类型 {type(t3)}')

t4 = 10, 20, 40
print(f't4 类型 {type(t4)}')
print(max(t4))
print(min(t4))
print(sum(t4))
print(len(t4))
print(sorted(t4))
#  升序降序 排序方式
print(sorted(t4, reverse=True))

print('test')

print('数组转元祖======')
t5 = tuple(list2)
print(type(t5))

print('********************************************************************')

func = lambda: 'hello liusc'
print(func())

lstData = [
    {'name': 'zhangsan', 'age': 19},
    {'name': 'lisi', 'age': 17},
    {'name': 'wangwu', 'age': 20}
]

lstData.sort(key=lambda x: x['age'])
print(lstData)
print('********************************************************************')
lstData.sort(key=lambda x: x['age'], reverse=True)
print(lstData)
print('********************************************************************')


# 定义函数：*nums 接收任意多个位置参数，自动打包成元组
def sum_num(*nums):
    # 定义累加初始值
    total = 0
    # 遍历元组，逐个累加
    for n in nums:
        total += n
    print(f"传入数字总和为：{total}")


# 调用测试：传任意个数数字
sum_num(1, 2)
sum_num(10, 20, 30)
sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum_num()  # 不传参数，总和为0


def test(x, y):
    a = x * y
    b = x + y
    return a, b


# 用一个变量去接收 那结果是元祖
print(test(2, 3))

# 多变量接收就是分别接收
a1, a2 = test(3, 4)
print(a1)
print(a2)

# 多变量接收就是分别接收
# ValueError: not enough values to unpack (expected 3, got 2)  注意长度问题
# a3,a4,a5=test(3,4)
# print(a3)
# print(a3)
# print(a5)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
list4 = [1, 2, 3, 4, 5]


# ** 是幂运算符（次方运算符）。
def func(x):
    return x ** 2


result = map(func, list4)
print(result)
print(list(result))


def funA(x, y):
    return x + y


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 归并结果集
print(reduce(funA, list4))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1111')

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 过滤出偶数
def funB(num):
    return num % 2 == 0


print(list(filter(funB, list5)))
# 排序
print(sorted(list5, reverse=True))

print(sorted([34, 78, -10, 6, 11]))  # 开序
print(sorted([34, 78, -10, 6, 11], reverse=True))  # 降序
print(sorted(['banana', 'apple', 'cucumber', 'demo']))
print(sorted(['Banana', 'apple', 'Cucumber', 'demo'], key=lambda str: str.lower()))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~12')
print(sorted(['Banana', 'apple', 'Cucumber', 'demo'], key=str.lower))
print(sorted(['aaaa', 'aaaaaaa', 'a', 'aa'], key=lambda str: len(str)))


