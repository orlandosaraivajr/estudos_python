# -*- coding: utf-8 -*-

# Singleton Clássico

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print(s)
s1 = Singleton()
print(s1)

# Singleton Clássico
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("Método __init__ chamado")
        else:
            print("Instância já criada", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
s1 = Singleton()
print(s1.getInstance())
print(s.getInstance())
print(s1.getInstance())

# Padrao Singleton Monostate

class Borg:
    __shared_state = {}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print("Objeto Borg b: ", b)
print("Objeto Borg b1: ", b1)
print("Estado de objetos de b: ", b.__dict__)
print("Estado de objetos de b1: ", b1.__dict__)
    
# Singleton com Metaclasses

class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1, logger2)
    
import sqlite3

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()
    
db1.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    