

def say_hello(name):
    # 定义内部函数
    def say(msg):
        print(f'对着{name}说:{msg}')

    return say

# 闭包
if __name__ == '__main__':
    alice = say_hello('Alice')
    alice('hello world')