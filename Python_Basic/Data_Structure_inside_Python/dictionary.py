# my_dic= {}
# my_dic= {1: 'abc', 2: 'xyz'}
# print(my_dic)
my_dict= {'name': 'ravi', 'add': 'bihar', 'age': 22}
# print(my_dict)
# my_dict= dict()
# my_dict= dict([(1,'abc'),(2,'xyz')])  # another way of creating dict
# print(my_dict)

# print(my_dict['name'])
print(my_dict.get('add'))   # print(my_dict['add])
# my_dict['name']='raushan'
# print(my_dict)
# my_dict['degree']= 'BTECH'
# print(my_dict)
# print(my_dict.pop('add'))
# print(my_dict)


# squares= {2:4, 3:9, 4:16, 5:25}
# my_dict= squares.copy()   # way to copy dict
# print(my_dict)

# subjects={}.fromkeys(['math','english','hindi'],0)  # when you want to init key with same valu at once
# print(subjects)


# method to get key-value pair(items), keys, values in a dictionary
# subjects= {2:4, 3:9, 4:16, 5:25}
# print(subjects.items())  # will print key-value pair in a list
# print(subjects.keys())   # will print keys  in a list
# print(subjects.values())  # will print values in a list


# #method for printing items in form of tuples
# for pair in subjects.items():
#     print(pair)


# new_dict= {k:v for k,v in subjects.items() if v>4}
# print(new_dict)

# d={k+ 1:v for k,v in subjects.items() if v>4}
# print(d)
# d={k+ 1:v*2 for k,v in subjects.items() if v>4}
# print(d)


#method1: to get the value of a specific key in Dictionary
# Dict = {1: 4, 2: 5, 3: 6}
# num=2
# for key,value  in Dict.items():
#     if(key==num):
#         print(Dict.get(key))
#         break

#method2: to get the value of a specific key in Dictionary
# Dict = {1: 4, 2: 5, 3: 6}
# nums= [3,2,1]
# for num in nums:
#         print(Dict[num])   #will give the value of key==num


# #method 1(best one,Time=o(n)): to get the key of a specific value in Dictionary
# subjects= {2:4, 3:9, 4:16, 5:25}
# key_list1= list(subjects)  # will store all values in a list
# key_list= list(subjects.keys())    # will store all keys in a list
# val_list= list(subjects.values())  # will store values in a list
# position=val_list.index(9)
# position1=val_list.index(4)
# print(key_list[position])   #will give the key of value==9
# print(key_list[position1])  # will give the key of value==4

#method 2 using dictionary.items(): to get the key of a specific value in Dictionary 
# subjects= {2:4, 3:9, 4:16, 5:25}
# def get_key(val):
#     for key, value in subjects.items():
#          if val==value:
#              return key
#     return "key doesn't exist"
# print(get_key(9))   
# print(get_key(4))
# print(get_key(25))


# to find a key value of a key and in case if key is not present
# then return a default value as specified 
# only by the help of get 

subjects= {2:4, 3:9, 4:16, 5:25}
print(subjects.get(2,-1))  # if there if no value for key '2'
                               # then it will return -1
print(subjects.get(1,-1))   # will return -1 since there is no val for key '1'
