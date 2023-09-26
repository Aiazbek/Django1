class Person:
    name = 'Nurbek'
    age = 16
    city = 'Bishkek'

    def say(self):
        return 'hello'


a = Person()
print(a.say())


class Car:
    name = 'Mercedes'
    model = 'GLE-coupe'
    capacity = 3.5
    color = 'White'
    wheels = 'x4 + 1'

    def sostoyanie(self):
        return 'very good!'


a = Car()
print(a.sostoyanie())


class car:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


a = car('Mercedes, GlE-Coupe', 3.5)
print(a.name, a.capacity)


class plus:

    def __init__(self, first, second):
        self.first = first
        self.second = second


a = plus(50, 100)
print(a.first + a.second)


class school:
    def __init__(self):
        pass


'''
Создайте класс BankAccount, который имеет атрибут balance. Используйте инкапсуляцию,
чтобы скрыть атрибут balance от прямого доступа извне класса,
но предоставьте методы deposit() и withdraw() для изменения баланса.
'''


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, saluu):
        if saluu > 0:
            self.balance += saluu
            print(f'Акчаныз ийгиликтуу депозитке кошулду! Азыркы учурда эсебиниз {self.balance}')
        else:
            print('Акча 0 дон чон болуусу керек! (Натуралдык сан)')

    def withdraw(self, aluu):
        if self.balance >= aluu:
            self.balance -= aluu
            print(f"Акчаныз ийгиликтуу чыгарылды! Азыркы учурда эсебиниз {self.balance}")
        else:
            print("Акчаны чыгаруу учун каражатыныз жетпейт!")

    def balance_now(self):
        return self.balance


nur = BankAccount()

kosh = int(input("Кошула турган сумма: "))
nur.deposit(kosh)

al = int(input("Алына турган сумма: "))
nur.withdraw(al)

now = nur.balance_now()
print(f'Азыркы учурда эсебиниз: {now}')
