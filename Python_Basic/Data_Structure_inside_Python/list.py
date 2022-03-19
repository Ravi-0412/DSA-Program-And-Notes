# lst=['one','two','three','four']
# lst1= [1,2,'ram']
# lst.append('five')

# lst.insert(2,'nine') # insert at specific location
# print(lst)

# lst.remove('two')   # will remove two from the list

# lst.append(lst1)  # will append the list1(in list form itself) at the last of lst
# lst.extend(lst1)  # will only append elements of lst1(not list form) in the lst 
# print(lst)

# del lst[1]   # will delete the ele at index '1' from the list
# print(lst)
# a= lst.pop(1)  # will delete the ele at index '1' from the list
# print(a)
# print(lst)

# lst=['one','two','three','four',1,2,3]
# if 'two' in lst:
#     print('hii')
# if 'six' not in lst:
#     print('hello')


# numbers= [3,1,6,2,8]
# numbers.sort()   # will sort the list in the given list itself(in place sorting)
                  # used when we don't need the original list
                  # this method 'sort' is only defined for list
# sorted(numbers)  # it returns a new sorted list ,so to get the sorted list you have to
                   # store the result in another list
                   # original list will be same as before only
# sorted_lst= sorted(numbers)  # this method 'sorted' accepts any iterable like string,set,tuple etc..
# print("sorted list: ", sorted_lst)
# print("original list: ", numbers)
# print("reverse ordered list: ", sorted(numbers,reverse=True))  # will sort  the list in the des order


# s="my name is Ravi Raushan"
# split_lst= s.split()  # return a list with words of string as elements
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
#  print(list1.count(10))   # will count the no of '10' in the given list

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
# my_list.extend('geeks') # will add whole string(single letters wise) to the end of the list
# print my_list
# output: ['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']


# reversing a list in python

# method 1: using list.reverse()
# method 2: using a= reversed(list)  # this method will return the object
# so in orderf to get the list youy will have to write:-  print(list(a))
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





# deleting a list or some elements of a list

# a= [1,2,3,4,5,6,7,8]
# del a[:]  # will delete whole list
# print(a)

a= [1,2,3,4,5,6,7,8]
# del a[2:]  # will delete everything from index 2
del a[2:-2]  # will delete everything from index 2 
            # to last two ele(won't delete last two ele)
print(a)

# a.clear()     # will delete whole list
# a= []      # another way to delete all ele
