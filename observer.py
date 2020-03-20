# -*- coding: utf-8 -*-

class Subject:
    def __init__(self):
        self.__observer = []
    
    def register(self, observer):
        self.__observer.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observer:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args,' from ' ,id(subject))

class Observer2:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args,' from ' ,id(subject))

subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)

subject.notifyAll('Notification')

##########################################################
##########################################################

class NewsPublisher:
    def __init__(self):
        self.__subscriber = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscriber.append(subscriber)
    
    def detach(self):
        return self.__subscriber.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscriber]

    def notifySubscribers(self):
        for sub in self.__subscriber:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News: ', self.__latestNews

from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnotherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())



news_publisher = NewsPublisher()

for Subscriber in [SMSSubscriber, EmailSubscriber, AnotherSubscriber]:
    Subscriber(news_publisher)

print('\n Subsctiber: ', news_publisher.subscribers())

news_publisher.addNews('Hello World')
news_publisher.notifySubscribers()

print('\n Detacher: ', type(news_publisher.detach()).__name__)
print('\n Subscribers: ', news_publisher.subscribers())


news_publisher.addNews('My Seccond news')
news_publisher.notifySubscribers()







