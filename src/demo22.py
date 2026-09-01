'''
猜数游戏
'''
import random

num = random.randint(1, 10)
print(num)

print('猜数游戏')

while True:
    input_num = int(input('猜一个数字'))
    if input_num > num:
        print('猜的数字大了')
    elif input_num < num:
        print('猜的数字小了')
    else:
        print('猜对了')
        break

