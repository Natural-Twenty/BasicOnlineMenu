#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:12:40 2019

@author: z5075710
"""

class Customer:
    
    def __init__(self, name, email, username, password):
        self._name = name
        self._email = email
        self._username = username
        self._password = password
        
    #Functions involving the customer's name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        print('Setting name') #For testing, comment/remove when done testing
        self._name = name
    
    #Functions involving the customer's email    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        print('Setting email') #For testing, comment/remove when done testing
        self._email = email
        
    #Functions involving the customer's username    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        print('Setting username') #For testing, comment/remove when done testing
        self._username = username
    
    #Functions invovling password    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        print('Setting password') #For testing, comment/remove when done testing
        self._password = password
        
        
    def __str__(self):
        message = ''
        message += f'Hello, {self._name}. Here are your details.\n'
        message += f'Email: {self._email}\n'
        message += f'Username: {self._username}\n'
        message += f'Password: {self._password}\n'
        return message