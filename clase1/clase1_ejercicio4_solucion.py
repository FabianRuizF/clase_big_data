import numpy as np
import functools

list_of_numbers = np.arange(10000000)

def square(x):
  return x*x

def add(x,y): 
  return x+y

%%timeit -n 10 -r 3
list_of_square = list(map(square,list_of_numbers))
print(functools.reduce(add, list_of_square))

%%timeit -n 10 -r 3


total=0
for number in list_of_numbers:
  square_number = square(number)
  total = total + square_number
print(total)


%%timeit -n 10 -r 3
pow_number = np.power(list_of_numbers,2)
print(np.sum(pow_number))
