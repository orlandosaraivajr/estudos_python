class Order:
    def __init__(self, value):
        self.__value = value
    @property
    def value(self):
        return self.__value


from abc import ABCMeta, abstractmethod

class Frete(metaclass=ABCMeta):
    @abstractmethod
    def calcular(self, order):
        pass

class FreteDefault(Frete):
    def calcular(self, order):
         return order.value * 0.05

class FreteExpress(Frete):
    def calcular(self, order):
         return order.value * 0.01


class CalculateShipping:
    def execute_calculation(self, order, shipping=FreteDefault() ):
        if issubclass(type(shipping), Frete):
            total = shipping.calcular(order)
            print(total)
        else:
            print('Falhou')

order = Order(500)
calculate_shipping = CalculateShipping()
calculate_shipping.execute_calculation(order, FreteExpress())
calculate_shipping.execute_calculation(order, FreteDefault())
calculate_shipping.execute_calculation(order)

class FreteFake:
        def calcular(self, order):
         return order.value * 0.01

calculate_shipping.execute_calculation(order, FreteFake())





        

