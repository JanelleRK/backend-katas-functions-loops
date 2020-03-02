#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Janelle Kuhns with help on multiply from J. Hyuck"


def add(x, y):
    add_num = x + y
    return add_num

print(add(2,4))

def multiply(x, y):
    counter = 0
    for _ in range(abs(y)):
        counter = add(counter,x)
    if y < 0:
        return 0 - counter
    return counter

print(multiply(4, -8))

def power(x, n):
    counter = x
    for _ in range(n-1):
        counter = multiply(counter, x)
    return counter

print(power(2,8))

def factorial(x):
    result = 1
    for i in range(x):
        result += multiply(result, i)
    return result

print(factorial(4))


def fibonacci(n):
    first_num = 0
    second_num = 0
    number = 0
    for i in range(n+1):
        if i == 0:
            continue
        elif i == 1:
            number = add(number, 1)
            second_num = number
        else:
            number = add(first_num, second_num)
            first_num = second_num
            second_num = number
    return number

print(fibonacci(8))


if __name__ == '__main__':
    # your code to call functions above
    pass
