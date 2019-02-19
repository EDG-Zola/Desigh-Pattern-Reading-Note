#coding=utf-8

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    '''
    主题类，抽象基类接口
    '''
    @abstractmethod
    def do_pay(self):
        pass
    

class Bank(Payment):
    '''
    实际主题类
    '''
    def __init__(self):
        self.card = None
        self.account = None
    
    def __getAccount(self):
        self.account = self.card # 为了简单，使用卡号作为账号信息
        return self.account
    
    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True
        
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds！")
            return False

class DebitCard(Payment):
    '''
    代理类Proxy
    '''
    def __init__(self):
        self.bank = Bank()
        
    def do_pay(self):
        card = input("Proxy:: Punch in card number: ") # 输入卡号信息
        self.bank.setCard(card) # 使用卡号信息初始化bank账号
        return self.bank.do_pay() #调用实际主题类对象bank的do_pay完成支付
    

class You:
    '''
    客户端类
    '''
    def __init__(self):
        print("You:: Let's buy Denim shirt!")
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    
    def __del__(self):
        '''
        析构函数
        '''
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more money :-(")

#if __name__=='__main__':
you = You()
you.make_payment()