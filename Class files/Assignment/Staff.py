#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:41:40 2019

@author: z5075710, The Minh Tran
"""
#Need to validate using isinstance(x, int)/(y, str)

class Staff:
    def __init__(self, username, password):
        self._order = []
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
    
    @order.setter
    def addOrder(self, order):
        print('Adding order') #For testing purposes, omment this line of code out once done
        self._order.append(order)
        
    @order.deleter
    def deleteOrder(self, order):
        if order in self._order:
            print('Deleting order') #For testing purposes, omment this line of code out once done
            self._order.remove(order)
        else:
            print('No order exists')