#practice practicum question 3

import random

random_number1 = random.randint(1,9)
random_number2 = random.randint(1,9)


def practice_addition(a,b):
    result = a+b
    print ('what is', (a), '+', (b),'?')
    answer = int(input())

    #if answer == result:
     #   return True
    #else:
   #     return False


    return answer == result
    
    


print(practice_addition(random_number1,random_number2))
    
