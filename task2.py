from random import randint,sample
def get_numbers_ticket(min,max,quantity):
    lotery_numbers = set()
    while len(lotery_numbers)<quantity:
        try:
           lotery_numbers.add(randint(min, max))
           print(sorted(sample(range(1, 1000), quantity)))
           break
        except TypeError:
            print("Not right format")
            break

get_numbers_ticket(1,49,6)