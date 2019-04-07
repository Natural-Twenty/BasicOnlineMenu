#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:41:40 2019

@author: z5075710, The Minh Tran
"""
#Need to validate using isinstance(x, int)/(y, str)
from Order import Order
class Staff:
    def __init__(self, username = None, password = None):
        self._order = []
        self._orderReady = []
        self._username = username
        self._password = password
        
        
    #Functions involving username
    @property
    def username(self):
        print('Getting username') #For testing purposes, omment this line of code out once done
        return self._username
    
    @username.setter
    def username(self, username):
        print('Setting username') #For testing purposes, omment this line of code out once done
        self._username = username
    
    #Functions involving password
    @property
    def password(self):
        print('Getting password') #For testing purposes, omment this line of code out once done
        return self._password
    
    @password.setter
    def password(self, password):
        print('Setting password') #For testing purposes, omment this line of code out once done
        self._password = password
        
    #Functions involving order
    @property
    def order(self):
        print('Getting order list') #For testing purposes, omment this line of code out once done
        return self._order
    
    
    def addOrder(self, order):
        print('Adding order ... \n') #For testing purposes, omment this line of code out once done
        self._order.append(order)
        
    @order.deleter
    def deleteOrder(self, order):
        if order in self._order:
            print('Deleting order') #For testing purposes, omment this line of code out once done
            self._order.remove(order)
        else:
            print('No order exists')
    
    @property
    def viewOrder(self):
        print(self._order[0])
        
    def viewAllOrder(self):
        for o in self._order:
            print(o)
        
    def setStatus(self, orderIndex, status = 'Ready'):
        print('Setting status ...\n')
        self._order[orderIndex].setStatus(status)
        self._orderReady.append(self._order[orderIndex])
        self._order.remove(self._order[orderIndex])
        
    def checkStatus(self, orderID):
        print('Checking status ... \n')
        if any(self._orderReady) is True:
            for o in range(0,len(self._orderReady)):
                if orderID is self._orderReady[o].orderID:
                    print(f'{self._orderReady[o].status}')
                else:
                        print('Not ready')
        else:
            print('Not ready')
        
        