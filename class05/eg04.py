class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我的名字是{self.name}，年龄是{self.age}")


class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major

    def say(self):
        super().say()
        print(f"我的专业是{self.major}")

s = Student('张三',20,'计算机')
s.say()