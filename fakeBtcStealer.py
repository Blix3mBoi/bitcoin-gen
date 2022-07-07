import random
import liststring
import time
alphabet = list('abcdefghijklmnopqrstuvw')
while True:
    list = []
    for i in range(20):
        if random.randint(1,5) <= 3:
            list.append(str(random.randint(0,9)))
        else:
            list.append(random.choice(alphabet))
    time.sleep(1)
    string = liststring.list_to_string(list)
    print(string)
