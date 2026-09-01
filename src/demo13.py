import traceback

def fun2(*args):
    print(args)


fun2(10, 20, 30)

def fac(n):
    if n==1:
        print("AA  n的值{}, n-1的值{}".format(n, n - 1))
        return 1
    else:
        print("BB  n的值{}, n-1的值{}".format(n,n-1))
        return n*fac(n-1)


print(fac(5))

print("***********************")
try:
    print("===========")
    print(10/0)
except:
    print("异常处理")
    traceback.print_exc()
