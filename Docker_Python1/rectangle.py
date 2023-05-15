#!/bin/python
import math

length = int(input('Enter rectangle length: '))
width = int(input('Enter rectangle width: '))

diagonal = math.sqrt(length**2 + width**2)
print(f'rectangle diagonal length is {diagonal}')