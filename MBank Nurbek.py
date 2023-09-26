class MBank:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__cash = 0
        self.__status_gold = False

    def Verification(self, documents_allowed: str):
        self.documents_allowed = documents_allowed
        if self.documents_allowed == 'yes':
            self.__status_gold = True
        else:
            self.documents_allowed = False

    def get_cash(self):
        return f'Ваш баланс в настоящее время {self.__cash} сом'

    def set_cash(self, plus: float):
        self.plus = plus
        if self.plus <= 0:
            return f'Невозможно пополнить сумму не превосходящее 0 сом'
        else:
            if self.plus <= 100000:
                self.__cash = self.__cash + self.plus
                return f'Операция прошла успешно! + {self.plus} сомов'
            else:
                if self.__status_gold == True:
                    self.__cash = self.__cash + self.plus
                    return f'Операция прошла успешно! + {self.plus} сомов'
                else:
                    return f'Ваш статус низкий, чтобы пополнить счет больше 100000 за раз!'

    def set_cash_purchase(self, minus: float):
        self.minus = minus
        if self.minus <= 0:
            return f'Невозможно списать {self.minus} сомов, повторите попытку!'
        else:
            if self.minus > self.__cash:
                return f'В вашем счёте недостаточно средсв, чтобы списать {self.minus} сомов'
            else:
                self.__cash = self.__cash - self.minus
                return f'С вашего счёта было списано - {self.minus} сомов'



go = MBank('Askar', 'Bolotbekov')
print(f'Пользователь {go.name, go.surname}')

'''написать в ковычку 'yes' если пользователь успешно прошел идентицикацию! ,
в противном случае статус пользователя будет с ограничениями до 100 000 сом за 1 пополнение'''
go.Verification('')


print(go.set_cash(100001))
print(go.set_cash(200))
print(go.set_cash_purchase(5))
print(go.get_cash())


'''
go.set_cash    - пополнение
go.set_cash_purchase  - снятие (перевод другим)
go.get_cash
'''