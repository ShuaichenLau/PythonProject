'''
函数可以添加属性
'''

def my_fun():
    print('i am a function ' )

my_fun.author='sss'
my_fun.version='1.2'
my_fun.desc='this is test function.'


print(my_fun.author)
print(my_fun.version)
print(my_fun.desc)


func = my_fun()

print(func is my_fun())
print(type(func))
print(id(func))
print(id(my_fun()))

