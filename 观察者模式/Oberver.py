#coding=utf-8

from abc import ABCMeta, abstractmethod

class NewsPublisher:
    '''
    主题类
    '''
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber):
        '''观察者调用此方法注册主题'''
        self.__subscribers.append(subscriber)
        
    def detach(self):
        '''调用此方法注销最新订阅的观察者，也可以重载注销指定的观察者'''
        return self.__subscribers.pop()
        
    def subscribers(self):
        '''调用此方法返回注册该主题的所有的观察者'''
        return [type(x).__name__ for x in self.__subscribers]
            
    def notifySubscribers(self):
        '''此方法调用注册该主题的所有的观察者的update()方法，用来接收最新消息'''
        for sub in self.__subscribers:
            sub.update()
            
    def addNews(self, news):
        self.__latestNews = news
        
    def getNews(self):
        return "Got News: ", self.__latestNews
    
    
class Subscriber(metaclass=ABCMeta):
    '''
    观察者接口的抽象基类
    '''
    @abstractmethod
    def update(self):
        pass
    
    
class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        '''构造函数首先用NewsPublisher对象初始化属性publisher，然后调用NewsPublisher对象的attach(subscriber)方法进行注册'''
        self.publisher = publisher
        publisher.attach(self)
        
    def update(self):
        '''通过拉模型返回NewsPublisher对象的getNews()方法，获取最新消息'''
        print(type(self).__name__, self.publisher.getNews())
    
    
class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        '''构造函数首先用NewsPublisher对象初始化属性publisher，然后调用NewsPublisher对象的attach(subscriber)方法进行注册'''
        self.publisher = publisher
        publisher.attach(self)
        
    def update(self):
        '''通过拉模型返回NewsPublisher对象的getNews()方法，获取最新消息'''
        print(type(self).__name__, self.publisher.getNews())
        
class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        '''构造函数首先用NewsPublisher对象初始化属性publisher，然后调用NewsPublisher对象的attach(subscriber)方法进行注册'''
        self.publisher = publisher
        publisher.attach(self)
        
    def update(self):
        '''通过拉模型返回NewsPublisher对象的getNews()方法，获取最新消息'''
        print(type(self).__name__, self.publisher.getNews())    
    
    
#####################客户端#####################################
if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subcriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subcriber(news_publisher) # 使用NewsPublisher对象实例化各个具体的观察者
    
    # 打印目前订阅该主题的所有观察者
    print("\nSubscribers: ", news_publisher.subscribers())
    
    # 添加最新消息，并通知所有的观察者
    news_publisher.addNews("Hello world!")
    news_publisher.notifySubscribers()
    
    # 注销最新订阅的观察者，并返回目前所有的观察者
    news_publisher.detach()
    news_publisher.subscribers()
    
    # 添加最新消息，并通知给目前所有的观察者 
    news_publisher.addNews("Second News!")
    news_publisher.notifySubscribers()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        