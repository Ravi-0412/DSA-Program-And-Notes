# https://www.geeksforgeeks.org/deque-in-python/

import collections
de= collections.deque([1,2,3])
de.append(4)
print ("The deque after appending at right is : ")
print (de)  # will add ele at last(right most)

de.appendleft(6)   # will add ele at left 
print ("The deque after appending at left is : ")
print (de)

de.pop()   # will delete one ele from last(right side)
print ("The deque after deleting from right is : ")
print (de)

# de.popleft()    # will delete one ele from left 
# print ("The deque after deleting from left is : ")
# print (de)

# some more operations
# import collections
# de= collections.deque([1,2,3,4,4,2,4])
# print(de.index(4,2,5))     # will return the 1st index of ele '4' in the range of index 2 to 5

# de.insert(4,3)     # will insert the ele '3' at index==4 i.e at 5th position
# print ("The deque after inserting 3 at 5th position is : ")
# print (de)

# print ("The count of 3 in deque is : ")
# print(de.count(3))   # will count the occurences of 3

# de.remove(3)    # remove the 1st occurences of '3'
# print(de)

# some more operations
# de.extend([5,6,7])      # will add multiple values to the deque at right 
# print(de)
# de.extendleft([8,9])    # will add multiple values to the deque at left
# print(de)

# de.rotate(-3)     # will roatate the deque given no of times
#                  # if no is negative then rotation occurs to the left
# print(de)

# de.rotate(2)    # will rotate to right by '2'
# print(de)  

# de.reverse()   # will reverse the deque
# print(de)