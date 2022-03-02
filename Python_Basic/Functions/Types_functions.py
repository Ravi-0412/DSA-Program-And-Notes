# num = -100
# print(abs(num))
# print(divmod(9,2))

# numbers= [10,20,30,40,50]
# for index,num in enumerate(numbers,5):
#     print("index {} has value {}".format(index,num))


# def find_positive_number(num):
#     if num>0:
#         return num

# number= range(-10,10)
# print(list(number))
# positive_num_list= list(filter(find_positive_number,number))
# print(positive_num_list)

# numbers= [10,20,30,40,50]
# print(isinstance(numbers,list))
# t= (1,2,3,4) 
# print(isinstance(t,list))


# numbers=[1,2,3,4]
# square= []
# for i in numbers:
#     square.append(i**2)
# print(square)

# numbers=[1,2,3,4]
# def powerOfTwo(num):
#     return num**2
# square=list(map(powerOfTwo,numbers))
# print(square)


from functools import reduce
numbers=[1,2,3,4]
def multiply(x,y):
    return x*y
product= reduce(multiply,numbers)
print(product)

