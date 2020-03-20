from abc import abstractmethod, ABCMeta

class Viagem(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retornarCasa(self):
        pass

    def itinerario(self):
        self.setTransport()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retornarCasa()


class ViagemSantos(Viagem):
    def setTransport(self):
        print('Ir de carro')

    def dia1(self):
        print('Ir para praia')

    def dia2(self):
        print('Ver o museu do café')

    def dia3(self):
        print('Ir para praia novamente')

    def retornarCasa(self):
        print('Comprar peixe')


class ViagemBahia(Viagem):
    def setTransport(self):
        print('Ir de avião')

    def dia1(self):
        print('Conhecer pelourinho')

    def dia2(self):
        print('Ir para praia')

    def dia3(self):
        print('Museus')

    def retornarCasa(self):
        print('Comprar acarajé')


class AgenciaViagem:
    def viagem(self):
        opcao = input('santos ou bahia?\n')
        if opcao == 'santos':
            self.viagem = ViagemSantos()
        if opcao == 'bahia':
            self.viagem = ViagemBahia()
        self.viagem.itinerario()

AgenciaViagem().viagem()
