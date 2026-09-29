def gen_exp():
    i = 2
    yield i
    while True:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            # 只有当上面的 for 循环把 range 全部测完了，都没触发 break
            # 才能证明 i 是一个真正的质数！
            yield i


gen = gen_exp()
print(type(gen))

for i in range(10):
    print(f'{i}__{next(gen)}')

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
