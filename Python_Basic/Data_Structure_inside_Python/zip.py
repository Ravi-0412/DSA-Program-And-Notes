#  zip() method takes iterable or containers and returns a single iterator object, 
#  having mapped values from all the containers.

# zip is used to map the similar index of multiple containers so that 
# they can be used just using a single entity. 

name= ("Navin", "Kumar", "Raju")
roll_no= (1,2,3)
marks= (90, 80, 70)

zipped = zip(name,roll_no,marks)  # will take index from same position and will map them
# zipped returns a zip object
# to print the data we need to convert it into a list, or dictionary,or tuple or set
# then it will print according to the property of the data type
# print(zipped)     # will print the address of zip object
# lst= list(zipped)  # converting zip object into list
# print(lst)
# dict1= dict(zipped)  # converting zip object into dictionary
# print(dict1)        # for more than 2 parameters, dictioanry will not work
# set1= set(zipped)  # converting zip object into set
# print(set1)

# for iterating in zip object
for a,b,c in zipped:  # a,b,c is the diff attributes like name, roll, marks
    print(a,b,c)    # will print the data in the order of the tuple each in new line

# or simply use 
# this method is valid for any type of data structure in python
for ele in zipped:
    print(ele)
