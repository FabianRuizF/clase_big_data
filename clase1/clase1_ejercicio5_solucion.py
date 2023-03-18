import multiprocessing.dummy as mp
import numpy as np
import functools

list_of_numbers = np.arange(10000000)

%%timeit -n 10 -r 3

with mp.Pool(processes=4) as p:
  pow_number = p.map(cube, list_of_numbers,chunksize=2000000)
print(functools.reduce(add, pow_number))
