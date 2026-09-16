class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print("Employee-print: 工号:{} 员工姓名:{}".format(self.id, self.name))


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


zhangsan = FullTimeEmployee("张三", 1, 8000)
lisi = PartTimeEmployee("李四", 2, 500, 20)

zhangsan.print_info()
lisi.print_info()


print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())

