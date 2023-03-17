%%timeit -n 3 -r 3
list_of_numbers = [x for x in range(10000000)]

%%timeit -n 3 -r 3
list_of_pair = []
list_of_odd =  []
for number in list_of_numbers:
    if(number%2==0):
      list_of_pair.append(number)
    if(number%2==1):
      list_of_odd.append(number)
      

#El codigo se puede optimizar haciendo lo siguiente
%%timeit -n 3 -r 3
list_of_numbers = np.arange(10000000)
#Dado que donde mas hay demoras es al momento de crear los numeros
