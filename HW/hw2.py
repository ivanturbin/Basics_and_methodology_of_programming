from random import randint
 
#20 случайных чисел в интервале [0:100]
random_list = [randint(0, 9999) for _ in range(randint(50, 100))]
 
print(random_list)