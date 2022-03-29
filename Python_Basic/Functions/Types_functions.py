# num = -100
# print(abs(num))
# print(divmod(9,2))

# numbers= [10,20,30,40,50]
# for index,num in enumerate(numbers,5):
#     print("index {} has value {}".format(index,num))


def find_positive_number(num):
    if num>0:
        return num

# filter() in python
# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a 
# sequence true or not.
# sequence: sequence which needs to be filtered, it can 
# be sets, lists, tuples, or containers of any iterators.
# Returns:
# returns an iterator that is already filtered.

number= range(-10,10)
print(list(number))
positive_num_list= filter(find_positive_number,number)  # stores the num that follows the function rule
print(positive_num_list)

# numbers= [10,20,30,40,50]
# print(isinstance(numbers,list))
# t= (1,2,3,4) 
# print(isinstance(t,list))


# numbers=[1,2,3,4]
# square= []
# for i in numbers:
#     square.append(i**2)
# print(square)


# map function
# map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
# NOTE : You can pass one or more iterable to the map() function.
numbers=[1,2,3,4]
def powerOfTwo(num):
    return num**2
square= map(powerOfTwo,numbers)
print(list(square))   # convert to any data structure for printing


# reduce function in python
# Working :  
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

from functools import reduce
numbers=[1,2,3,4]
def multiply(x,y):
    return x*y
product= reduce(multiply,numbers)  # 1st para is operations(or functions)
                                   # and second para is the list on which you want to apply that operations
print(product)

