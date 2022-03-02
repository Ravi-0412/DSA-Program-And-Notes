# s= {1,2,3}
# print(s)
# print(type(s))

# s= {1,2,3,4,1,2,1}
# print(s)

# converting list into set
# list1= [10,20,30,0,50,60,70,80,10,10]
# s= set(list1)
# print(s)

# s= set()
# print(type(s))

# adding elemenst to the set
s= {1,2,3}
s.add(4)
# update()
# Syntax :  set1.update(set2) 

# Here set1 is the set in which set2 will be added.

# Parameters : Update() method takes only a single argument. T
#the single argument can be a set, list, tuples or a dictionary.
# It automatically converts into a set and adds to the set before update()
s.update([5,6,7])
print(s)
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]
# Lists converted to sets
set1 = set(list2)  
set2 = set(list1)
# Update method
set1.update(set2)  #will add the values of set2 to set1
# Print the updated set
print(set1)
 
# List is passed as an parameter which
# gets automatically converted to a set
set1.update(list3)
print(set1)

# s= {1,2,3,4,5,6,7,8}
# s.discard(3)
# print(s)

# s1= {1,2,3,4,5,6,7,8}
# s2= {3,4,9,10,5,7,11}
# # print(s1 | s2)   # union
# print(s1.union(s2))
# print(s1 & s2)   # intersection
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2)) # can use '^' operator also


x= {1,2,3,4,5,6,7}
y= {3,6,7}
print("set 'y' is subset of 'x' ?= ",y.issubset(x))
print("set 'x' is subset of 'y' ?= ",x.issubset(y))