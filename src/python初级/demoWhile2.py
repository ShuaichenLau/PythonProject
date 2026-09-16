from Student import Student

zhangsan = Student("zhangsan", 11, 202001)
lisi = Student("lisi", 12, 202002)

student_list = [zhangsan, lisi]
student_list2 = {zhangsan, lisi}

print(type(student_list))
print(student_list)

for item in student_list:
    print(id(item))
    print(item.speak())

print(type(student_list2))

scores={'zhangsan':100,'lisi':99,'wangwu':98}
print(scores['zhangsan'])
print(scores.get("zhangsan"))
print(scores.get("zhangsan1"))

# 如果获取的key不存在, 则返回0000000 默认值
print(scores.get("zhangsan1",0000000))
print(scores.get("zhangsan",11))

print(type(scores.get("zhangsan1")))
print("========================================================================")

print("zhangsan" in scores)
print("zhangsan2" in scores)

if "zhangsan2" in scores:
    print("zhangsan2 in scores")
else:
    scores["zhangsan2"]=19999
    print(scores["zhangsan2"])

print(type[scores])
lst = scores.items()
print(type(lst))