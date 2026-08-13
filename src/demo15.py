import math


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('{} 汽车已经启动'.format(self.brand))

    def stop(self):
        print('{} 汽车已经停止'.format(self.brand))


bmw=Car('BMW_X3')
bmw.start()

print(dir(bmw))


print(id(math))
print(type(math))

print(math)
print(math.pi)

print(math.log2(2))