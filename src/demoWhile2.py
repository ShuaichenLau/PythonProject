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
