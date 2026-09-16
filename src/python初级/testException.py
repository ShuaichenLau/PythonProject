try:
    user_weight = float(input("Enter your weight:"))
    user_height = float(input("Enter your height:"))
    user_BMI = user_weight / (user_height ** 2)
    print("BMI:", user_BMI)
except ValueError:
    print("输入不为合理数字, 请重新运行程序, 并输入正确的数字")
except ZeroDivisionError:
    print("身高不能为0, 请重新运行程序, 并输入正确的数字")
except:
    print("发生未知错误, 请重新运行程序")
finally:
    print("程序结束")
