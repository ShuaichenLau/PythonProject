'''
遍历字符串
'''

str='asdfghjkl'

# for tiem in str:
#     print(tiem)


lst=['11',1,True]
print(f'集合长度是{len(lst)}')
print(lst)

# list集合可以存放不同类型的数据,是可变数组


list2=[1,2,'he,aa',['11','22'],'aa']
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
t1=()
t2=tuple()

print(type(t1))
print(type(t2))

t3=(1,2,'he,aa',['11','22'],'aa')
print(f't3 类型 {type(t3)}')

t4=10,20,40
print(f't4 类型 {type(t4)}')
print(max(t4))
print(min(t4))
print(sum(t4))
print(len(t4))
print(sorted(t4))
#  升序降序 排序方式
print(sorted(t4,reverse=True))


print('数组转元祖======')
t5=tuple(list2)
print(type(t5))



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
sum_num()   # 不传参数，总和为0


