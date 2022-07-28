class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def talk():
        print(f'반갑습니다.입니다.')


class Student(Person):
    @staticmethod
    def talk():
        print(f'저는 학생입니다.')
        super().talk()


s1 = Student('박승재')
s1.talk()
