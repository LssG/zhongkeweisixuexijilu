class Person:
    def fun1(self,mes):
        print (mes)

    @classmethod
    def fun2(cls):
        print("asd")


    @classmethod
    def fun3(cls):
        cls.fun2()

    @staticmethod
    def fun4():
        Person.fun2()

class Student(Person):
    def __init__(self):
        pass

    @classmethod
    def fun2(cls):
        print("uiou")

p = Person()
p.fun1("fkjdshkl")

Person.fun4()
Student.fun3()