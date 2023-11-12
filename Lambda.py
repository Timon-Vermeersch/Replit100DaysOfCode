# def double(x): return x *2
# def add(x, y): return x + y
# def product(x, y, z): return x * y * z
from functools import reduce
double = lambda x : x * 2
add = lambda x , y : x + y
product = lambda x, y, z : x * y * z

myList = [2,4,5,6,7,8]
myList2 = [2,6,5,6,7,8]

a = map(lambda x : x * 2,myList)
print(list(a))
b = map(lambda x , y : x + y, myList,myList2 )
for item in list(b):
    print(item , end = " | ")

c = filter(lambda x : x%2 ==0,myList)
print(list(c))

d = filter(lambda x : True if x>=5 else False, myList)
print(list(d))


e = reduce(lambda x,y: x+y ,myList)
print(e)
