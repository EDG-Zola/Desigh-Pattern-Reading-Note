#coding=utf-8

from abc import ABCMeta, abstractmethod

class Agent:
    '''
    Invoker调用者
    '''
    def __init__(self):
        self.__orderQueue = []
        
    
    def placeOrder(self, order):
        '''调用者拥有一个命令对象列表，在某个时刻调通过此方法调用命令对象的execute()方法，将请求付诸实行'''
        self.__orderQueue.append(order)
        order.execute()
        
    

class StockTrade:
    '''
    Receiver接受者，是一个知道如何做必要的工作的类
    '''
    def buy(self):
        print("You will buy stocks.")
        
    def sell(self):
        print("You will sell stocks.")
        
        
class Order(metaclass=ABCMeta):
    '''
    命令Command的抽象基类，即为具体的命令类提供了一个接口
    '''
    @abstractmethod
    def execute(self):
        '''通过调用命令对象的execute()方法，可以让接收者进行相应的工作'''
        pass
    
    
class BuyStockOrder(Order):
    '''具体命令对象类'''
    def __init__(self, stock):
        '''通过此方法将接收者绑定'''
        self.stock = stock
        
    def execute(self):
        '''命令执行方法，通过调用此方法`发出命令执行请求`，然后`调用接收者的一个或多个动作`,由`接收者执行请求`'''
        self.stock.buy()
    
    
class SellStockOrder(Order):
    '''具体命令对象类'''
    def __init__(self, stock):
        '''通过此方法将接收者绑定'''
        self.stock = stock
        
    def execute(self):
        '''命令执行方法，通过调用此方法`发出命令执行请求`，然后`调用接收者的一个或多个动作`,由`接收者执行请求`'''
        self.stock.sell()
    
    
#####################客户端#####################################
if __name__ == '__main__':
    # Client
    stock = StockTrade() # 客户先实例化一个接收者对象
    buyStock = BuyStockOrder(stock) # 然后将接收者对象与具体的命令对象绑定起来
    sellStock = SellStockOrder(stock) # 将接收者对象与具体的命令对象绑定起来
    
    # Invoker
    agent = Agent() # 实例化一个调用者对象
    agent.placeOrder(buyStock) # 将命令对象与调用者绑定起来，调用者`发出命令执行请求`
    agent.placeOrder(sellStock) # 将命令对象与调用者绑定起来，`发出命令执行请求`
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        