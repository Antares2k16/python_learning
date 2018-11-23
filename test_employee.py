#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:08:46 2018

@author: aliao
"""

import unittest
from employee_info import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    
    def setUp(self):
        """Create an employee for use in all test methods."""
        
        self.my_employee = Employee("bob", "jefferson")
        
    def test_give_default_raise(self):
        """Test if salary raises by default amount"""
        
        self.my_employee.give_raise()
        self.assertEqual(self.salary, 72000)
        
    def test_give_custom_raise(self):
        """Test if salary raises by custom amount"""
        
        self.my_employee.give_raise(1000)
        self.assertEqual(self.salary, 68000)
        
unittest.main()
        