#!/usr/bin/env python3

"""Calculator Module
This module provides basic arithmetic operations such as addition, subtraction, 
multiplication, and division.
"""
#Design Calculator Module which will have functions for add, sub, mul, div
def add(num1, num2):
    '''Docuemnt of Function: add two numbers'''
    print("Adding two numbers:", num1, num2)
    return  int(num1) + int(num2)

def sub(num1, num2):
    '''Docuemnt of Function: sub two numbers'''
    print("Subtracting two numbers:", num1, num2)
    return int(num1) - int(num2)

def mul(num1, num2):
    '''Docuemnt of Function: multiply two numbers'''
    print("Multiplying two numbers:", num1, num2)
    return int(num1) * int(num2)

def div(num1, num2):
    '''Docuemnt of Function: divide two numbers'''
    print("Dividing two numbers:", num1, num2)
    if int(num2) == 0:
        return "Division by zero is not allowed"
    return int(num1) / int(num2)

