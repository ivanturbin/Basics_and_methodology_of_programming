from random import randint

def magic(x):
    num = [randint(0,9999) for i in range(randint(5, 101))]
    nums = 0
    for i in num:
        nums += i
    if nums % x == 0:
        nums = True
    else:
        nums = False
    return nums
x = random.randint(1, 9999)
print(magic(x))