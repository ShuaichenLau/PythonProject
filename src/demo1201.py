
class person:
    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id
    def __str__(self):
        print('ID是{}, 名字是{}, 年龄是{}'.format(self.id, self.name, self.age))

stuA = person(101, 'alice', 18)
stuB = person(102, 'aliceA', 20)

stuA.__str__()
stuB.__str__()


stuA.name='aliceAB'
stuA.__str__()