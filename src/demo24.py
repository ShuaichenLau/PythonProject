class Student:
    school = "第一实验中学"  # 类属性（所有实例共享）

    def __init__(self, name, age):
        self.name = name     # 实例属性
        self.age = age

    # 1. 实例方法：通过 self 操作当前实例的状态
    def introduce(self):
        print(f"我是 {self.name}，来自 {self.school}")

    # 2. 类方法：通过 cls 访问或修改类本身的状态，常作为工厂方法构造对象
    @classmethod
    def create_from_string(cls, info_str):
        # 接收 "Tom,18" 这样的字符串，并返回一个新实例
        name, age = info_str.split(",")
        return cls(name, int(age))

    # 3. 静态方法：不需要访问 self 或 cls，只是挂在类命名空间下的工具函数
    @staticmethod
    def is_adult(age):
        return age >= 18


# --- 测试调用 ---
s1 = Student("Alice", 17)
s1.introduce()  # 调用实例方法

s2 = Student.create_from_string("Bob,20")  # 类方法作为工厂
s2.introduce()

print(Student.is_adult(20))  # 静态方法，逻辑独立