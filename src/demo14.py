class Student:
    native_pace = '吉林'

    def eat(self):
        print('学生{}在吃饭..'.format(self.name))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def method():
        print("我使用了staticMethod进行修饰, 所以我是静态方法")

    @classmethod
    def cm(cls):
        print('我是类方法 使用了classmethod修饰')


def drink():
    print('喝水..')



stu1 = Student('哈哈',22)
stu2 = Student('嗯嗯',22)
print(id(stu1))
print(type(stu1))
print(stu1)

stu1.eat()
print(stu1.native_pace)

Student.eat(stu1)
Student.eat(stu2)




