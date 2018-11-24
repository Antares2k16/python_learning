#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:49:13 2018

@author: aliao
"""

class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self, boost=5000):
        self.boost = boost
        self.salary += self.boost
    