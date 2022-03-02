# double= lambda x: x*2
# print(double(5))

lst= [1,2,3,4,5]
even_list= list(filter(lambda x:x % 2 ==0,lst))
print(even_list)

lst= [1,2,3,4,5]
new_list= list(map(lambda x: x ** 2, lst))
print(new_list)

from functools import reduce
lst= [1,2,3,4,5]
new_list= reduce(lambda x,y:x*y,lst)
print(new_list)