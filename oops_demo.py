class person:#class defination

    def __init__(self, name, age, hight, gender):
        self.name = name
        self.age = age
        self.hight = hight
        self.gender = gender #attributes

    def walk(self): #methods
        print(self.name, 'is walking')

    def talk(self):
        print(self.name, 'is talking')

    def listen(self):
        print(self.name, "is listening ")

b = person('mr.B', age=60, hight=5.5, gender='M')# intanciation of object
b.age = 61
print(b.age)
print(b.name)
b.walk()
b.talk()

sharath = person(name='sharath', age=18, hight=6, gender='M')
print(sharath.name)
sharath.listen()

