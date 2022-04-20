class Box:
    def __init__(self):
        print('Construtor')
    def quadrado(self):
            print('quadrado')
    def circulo(self):
            print('circulo')
    def esfera(self):
            print('esfera')

class Adapter:
    def __init__(self, ip):
        self._ne = Box()

    def __getattr__(self, item):
        if item in ('esfera','circulo'):
            return getattr(self._ne, item)
        raise Exception('Método não migrado')

a = Adapter('') 
a.circulo()
a.quadrado() 
