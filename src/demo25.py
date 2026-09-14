'''

计算阶乘
6!=6*5*4*3*2*1
'''


def factorial(num):
    if num < 0:
        raise ValueError("负数没有阶乘")
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(factorial(6))
