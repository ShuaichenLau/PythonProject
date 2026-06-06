class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def __str__(self):
        return "Student: " + self.name + " " + str(self.age)

    def speak(self):
        return "Student: " + self.name + " 在上课"

    # 在 Python 3.6 及以上版本中，强烈推荐使用 f-string。你只需要在字符串前面加一个 f，然后把变量放在花括号 {} 里，Python 会自动帮你把它们转换成字符串并拼好：
    def out_grades(self):
        return f"Student: {self.student_id} {self.name} 的成绩是：  {self.grades}"

    def out_grades_format(self):
        return "Student-format: {} {} 的成绩是：{}".format(self.student_id, self.name, self.grades)

    def print_grades(self):
        print("Student-print: " + self.student_id + " " + self.name + "的成绩是：" + str(self.grades))

    def for_print_grades(self):
        print(self.grades.items())
        print(self.grades.keys())
        print(self.grades.values())
        for course, grade in self.grades.items():
            print("Student: " + self.student_id + " " + self.name + "的" + course + "成绩是：" + str(grade))

    def set_grade(self, course, grade):  # 更新设置科目成绩
        if course in self.grades:
            self.grades[course] = grade
        else:
            print("Student: " + self.name + " 没有" + course + "课程")


if __name__ == '__main__':
    mike = Student("Mike", 18, "2019001")
    alice = Student("alice", 19, "2019002")
    print(mike)
    print(mike.speak())

    # print(alice.name)
    print(alice.out_grades())
    alice.set_grade("语文", 80)
    print(alice.out_grades())
    print(alice.out_grades_format())

    alice.print_grades()

    print("----------------------------------")

    alice.for_print_grades()
