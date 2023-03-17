
list_of_numbers = [x for x in range(10000000)]

list_of_pair = []
list_of_odd =  []
for number in list_of_numbers:
    if(number%2==0):
      list_of_pair.append(number)
    if(number%2==1):
      list_of_odd.append(number)
