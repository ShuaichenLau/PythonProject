# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

greet = "Hello "


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(greet + 'PyCharm')
    print_hi(greet + "liushuaichen")

    test_x = 0
    print(type(test_x))
    print(id(test_x))  # 判断内存地址用的
    test_x = "hello"
    print(type(test_x))
    print(id(test_x))
    if str == type(test_x):
        print("test_x 类型发生了改变")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
