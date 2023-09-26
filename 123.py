"""
ООП- обьектно ориентированное программирование:
                                                Инкапсуляция;
                                                Абстракция;
                                                Полиморфизм;
                                                Наследование;
             |Public -> публичный (hello)
Инкапсуляция |Protected -> защищённый (__hello)
             |Private -> приватный (_hello)

"""

"""get-алуу, set-oзгортуу киргизуу"""
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def get_name(self):
#         return self._name, self._age
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, age):
#         self._age = age
#
#
# per = Person('Sanjar', 16)
# per.set_age(17)
# per.set_name('Sanjarbek')
# # print(per.get_age())
# print(per.get_name())

"""@ - декораторы"""
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, new_age):
#         self._age = new_age
#
#
# per = Person('Nurik', 17)
# print(per.name)
# per.name = 'Ayaz'
# print(per.name)


# class MBank:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname
#         self.__cash = 0
#         self.__gold = False
#
#     def __verification(self):
#         self.__gold = True
#
#     def get__cash(self):
#         return f'Balance {self.__cash} som'
#
#     def set__cash(self, x):
#         self.__cash = self.__cash + x
#
#     def info(self):
#         return f'Name:{self.name}\nSurname:{self.surname}'
#
#     def shopping(self, x):
#         if self.__cash >= x:
#             if x <= 100_000:
#                 self.__cash = self.__cash - x
#                 return 'Udacha'
#             else:
#                 if self.__gold:
#                     self.__cash = self.__cash - x
#                     return f'баланс жетti'
#                 else:
#                     return 'Ваш статус низок'
#         else:
#             return f"jetpey atat {self.get__cash()}"
#
#     def get_gold(self):
#         if self.__gold:
#             return 'status GOLD'
#         else:
#             self.__verification()
#             return 'USPESHNO'
#
#
# online = MBank('Sanjar', 'Ayazov')
# print(online.info())
# print(online.get__cash())
#
# online.set__cash(100000)
# print(online.shopping(101000))
# print(online.get__cash())


""""
    Home work 2

    Добавьте комиссию на транзакции.
    Если сумма транзакции меньше 100 000 сом то комиссия составит 3%
    Если сумма транзакции больше 100 000 сом то комиссия составит 100 сом + 1.2%

1000 - 1030
1_000_000 - 100 + 1200 = 1300 => 1_001_300
"""

"""
дополнительное ДЗ
что такое декораторы, 
что такое сеттеры и геттеры, 
public, protected, private - сделайте пример
"""



