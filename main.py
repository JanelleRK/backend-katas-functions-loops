#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    add_num = x + y
    return add_num
print(add(2,4))
    


def multiply(x, y):
    counter = 0
    for i in range(x):
        counter = add(i, x)
    return counter
print(multiply(6, -8))


def power(x, n):
    power_num = x ** n
    return power_num


def factorial(x):
    return


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
