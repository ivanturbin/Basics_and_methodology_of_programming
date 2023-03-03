from random import randint

randomlist = [randint(0, 9999) for i in range(randint(50, 100))]
 
a = randomlist
def common(lst1): 
    return list(set(lst1))
e=common(a)
print(e)
print(randomlist)