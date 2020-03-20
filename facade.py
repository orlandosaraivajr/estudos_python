# -*- coding: utf-8 -*-

class EventManager:
    def __init__(self):
        print("Event Manager:: Let me talk to the folks")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        
        self.caterer = Caterer()
        self.caterer.setCuisine()
        
        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier:
    def __init__(self):
        print("Arranging the Hotel for marriage? --")

    def __isAvaliable(self):
        print("Is the Hotel free for the event on given day? ")
        return True

    def bookHotel(self):
        if self.__isAvaliable():
            print("Registered the Booking")


class Florist:
    def __init__(self):
        print("Flowers Decorations for an Event ? --")

    def setFlowerRequirements(self):
        print("Roses and Lilies would be used")

class Caterer:
    def __init__(self):
        print("Food for an Event ? -- ")

    def setCuisine(self):
        print("Chinese & Continental Cuises to be served \n\n")


class Musician:
    def __init__(self):
        print("Musical Arrangement for the Marriage --")

    def setMusicType(self):
        print("Jazz and Classical will be played \n\n")


class You:
    def __init__(self):
        print("You: Whoa ! Marriage Arrangements ??? ")
    
    def askEventManager(self):
        print("\nYou: Let's contact the Event Manager \n")
        em = EventManager()
        em.arrange()
    
    def __del__(self):
        print("You: Thank you Event Manager ")

you = You()
you.askEventManager()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        