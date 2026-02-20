class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print("Привет, меня зовут", self.name)
        print("Моя профессия:", self.profession)


class Classmate(Person):
    def __init__(self, name, profession, group_name):
        super().__init__(name, profession)
        self.group_name = group_name

    def introduce(self):
        print("Привет, меня зовут", self.name)
        print("Я одноклассник")
        print("Моя профессия:", self.profession)
        print("Моя группа:", self.group_name)


class Friend(Person):
    def __init__(self, name, profession, hobby):
        super().__init__(name, profession)
        self.hobby = hobby

    def introduce(self):
        print("Привет, меня зовут", self.name)
        print("Я друг")
        print("Моя профессия:", self.profession)
        print("Моё хобби:", self.hobby)


classmate1 = Classmate("Бектур", "Студент", "Python-21")
classmate2 = Classmate("Айбек", "Студент", "Python-21")

friend1 = Friend("Алмаз", "Программист", "Игры")
friend2 = Friend("Руслан", "Дизайнер", "Рисование")


classmate1.introduce()
print()

classmate2.introduce()
print()

friend1.introduce()
print()

friend2.introduce()
