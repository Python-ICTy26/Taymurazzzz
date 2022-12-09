class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def __str__(self):
        return 'соси хуй ' + human1.name + ', которому ' + str(human1.age) + ' лет'

    def get_name(self):
        return 'Меня зовут ' + human1.name

    def get_age(self):
        return 'Мне ' + str(human1.age)
human1 = Human('tigran', 17)
print(human1.age)
human1.birthday()
print(human1.age)
print(human1)
print(human1.get_name())
print(human1.get_age())