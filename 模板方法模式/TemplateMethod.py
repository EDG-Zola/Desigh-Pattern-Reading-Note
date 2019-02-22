#coding=utf-8

from abc import ABCMeta, abstractmethod

class Trip(metaclass=ABCMeta):
    '''
    抽象类，即为具体子类提供了一个接口
    '''
    @abstractmethod
    def setTransport(self):
        '''抽象方法，由具体子类来实现，调用此方法设置出行的交通工具'''
        pass
    
    @abstractmethod
    def day1(self):
        '''抽象方法，由具体子类来实现，调用此方法设置出行第一天浏览地点'''
        pass
    
    @abstractmethod
    def day2(self):
        '''抽象方法，由具体子类来实现，调用此方法设置出行第二天浏览地点'''
        pass
    
    @abstractmethod
    def day3(self):
        '''抽象方法，由具体子类来实现，调用此方法设置出行第三天浏览地点'''
        pass
    
    @abstractmethod
    def returnHome(self):
        '''抽象方法，由具体子类来实现，调用此方法设置返程需要做的事'''
        pass
    
    def itinerary(self):
        '''模板方法，此方法封装了完整的行程算法，具体的方法由子类实现'''
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()
    
    
class VeniceTrip(Trip):
    '''
    具体子类，实现抽象类的抽象方法
    '''
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")
    
    def day1(self):
        print("Visit St Mark's Basilica in St Mark's Square")
    
    def day2(self):
        print("Appreciate Doge's Palace")
    
    def day3(self):
        print("Enjoy the food near the Rialto Bridge")
    
    def returnHome(self):
        print("Get souvenirs for friends and get back")
    
    
class MaldivesTrip(Trip):
    '''
    具体子类，实现抽象类的抽象方法
    '''
    def setTransport(self):
        print("On foot, on any island, Wow!")
    
    def day1(self):
        print("Enjoy the marine life of Banana Reef")
    
    def day2(self):
        print("Go for the water sports and snorkelling")
    
    def day3(self):
        print("Relax on the beach and enjoy the sun")
    
    def returnHome(self):
        print("Dont feel like leaving the beach")
    

class TravelAgency:
    '''
    Client类
    '''
    def arrange_trip(self):
        '''此方法判断让客户选择历史旅行还是沙滩旅行，然后实例化一个具体子类对象，调用封装了算法的模板方法'''
        choice = input("What kind of place you'd like to go historical or to a beach? ")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        elif choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()
           
#####################客户端#####################################
if __name__ == '__main__':
   travelAgency = TravelAgency()
   travelAgency.arrange_trip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        