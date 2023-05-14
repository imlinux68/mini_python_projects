#!/bin/python

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

for i in range(10):
    print(f'{i + 1}\t Sum of {a} and {b} is {sum(a, b)}')
