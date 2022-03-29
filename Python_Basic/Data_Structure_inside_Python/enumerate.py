l1= ["eat","sleep","repeat"]
print(enumerate(l1))   # won't work as it returns an object like a zip function
# l2= enumerate(l1)   # will assign the index like 0,1,2.. to each element
# print(l2)    # will print the address of the object, for printin you hvae to chnage any data types like in case of zip()
# l3= list(enumerate(l1))
# print(l3)
l4= dict(enumerate(l1))
print(l4)

# iterating in enumerate object
for ele in enumerate(l1):
    print(ele)

# for changing the starting index and printing separately
for count,ele in enumerate(l1,100):  # will assign the index from 100
    print(count,ele)

# for getting desired output from the tuple
# this method is also valid for any data structure in python
for count,ele in enumerate(l1):
    print(count)
    print(ele)
