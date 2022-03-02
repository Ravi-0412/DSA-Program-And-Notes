# lst=['one','two','three','four']
# lst1= [1,2,'ram']
# lst.append('five')

# lst.insert(2,'nine') # insert at specific location
# print(lst)

# lst.remove('two') 

# lst.append(lst1)
# lst.extend(lst1)
# print(lst)

# del lst[1]
# print(lst)
# a= lst.pop(1)
# print(a)
# print(lst)

# lst=['one','two','three','four',1,2,3]
# if 'two' in lst:
#     print('hii')
# if 'six' not in lst:
#     print('hello')


# numbers= [3,1,6,2,8]
# sorted_lst= sorted(numbers)
# print("sorted list: ", sorted_lst)
# print("original list: ", numbers)
# print("reverse ordered list: ", sorted(numbers,reverse=True))


# s="my name is Ravi Raushan"
# split_lst= s.split()
# print(split_lst)


# numbers= [10,20,30,0,50,60,70,80]
# print(numbers[:])
# print(numbers[0:4])
# print(numbers[::2])
# print(numbers[2::2])


# method 1: adding two list
# list1= [10,20,30,0,50,60,70,80,10,10]
# list2=[1,2,3,4]
# new_list= list1 + list2
# print(new_list)
#  print(list1.count(10))

# method2 : to add list
# using extend() function
'''
The Python’s List extend() method iterates over an iterable like string, 
list, tuple, etc., and adds each element of the iterable to the end of List.
The length of the list increases by the number of elements present in the iterable.
Syntax: list.extend(iterable)

Parameters:

iterable: Any iterable (list, set, tuple, etc.)
Returns:

The extend() method modifies the original list. It doesn’t return any value.
'''
my_list = ['geeks', 'for']  
# Another list
another_list = [6, 0, 4, 1] 
# Using extend() method
my_list.extend(another_list)
print(my_list)

# e.g: 2
my_list = ['geeks', 'for', 'geeks']
my_tuple = ('DSA', 'Java')
my_set = {'Flutter', 'Android'} 
# Append tuple to the list
my_list.extend(my_tuple)  
print(my_list)  
# Append set to the list
my_list.extend(my_set)
print(my_list)

# e.g: 3
# my_list = ['geeks', 'for', 6, 0, 4, 1]  
# # My string
# my_list.extend('geeks') 
# print my_list
# output: ['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']


# reversing a list in python
# method 1: using list.reverse()
# method 2: using list1= reversed(list)
# method 3: list1= list[::-1]


# square= []
# for i in range(10):
#     square.append(i**2)
# print(square)


# square=[i**2 for i in range(10)]
# print(square)


# list2=[1,2,3,4]
# new_list=[i*2 for i in list2]
# print(new_list)


# numbers= [10,20,-30,0,-50,60,70,80]
# new_list= [i for i in numbers if i>=0]
# print(new_list)


# new_list= [(i,i**2) for i in numbers]
# print(new_list)


matrix= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# transpose= []
# for i in range(4):
#     lst= []
#     for row in matrix:
#         lst.append(row[i])
#     transpose.append(lst)
# print(transpose)

# concise way of finding the transpose of a matrix
transposed= [[row[i] for row in matrix] for i in range(4)]
print(transposed)


# iterating for num directly in list for specific range
arr = [17,18,5,4,6,1]
n= len(arr)
k=1
for num in arr[k:4]:  # in this only num iterate, index always remains same
                      # for operation related with index, you have to 
                      # increment index separately
    print(num)
    #k+= 1
print(k)  # will print 1 only


# for finding maximum, minimm etc for a specific range in any data supported data structure of python
arr = [4,9,8,4,7,10,1,15]
n= len(arr)
k=max(arr[2:])
j= max(arr[4:7])
p= max(arr[1:5])
r= max(arr[5:7])
print(k)
print(j)
print(p)
print(r)