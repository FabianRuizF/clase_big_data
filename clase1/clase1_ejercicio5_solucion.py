import multiprocessing.dummy as mp

%%timeit -n 10 -r 3

with mp.Pool(processes=4) as p:
  pow_number = p.map(cube, list_of_numbers,chunksize=2000000)
sum(pow_number)
