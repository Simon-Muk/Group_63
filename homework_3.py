class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        print("Привет, меня зовут", self.name)
        print("Моя профессия:", self.occupation)

        if self.higher_education:
            print("У меня есть высшее образование")
        else:
            print("У меня нет высшего образования")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print("Я одноклассник")
        print("Моя группа:", self.group_name)


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print("Я друг")
        print("Моё хобби:", self.hobby)


# Проверка работы
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "Python-21")
cl1.introduce()

print()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "Футбол")
fr1.introduce()