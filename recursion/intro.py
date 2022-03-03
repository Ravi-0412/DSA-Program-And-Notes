# example 1:
# class Numbers:
#     # write a function that takes a number and prints it
#     # print 5 numbers: 1 2 3 4 5 
#     def print1(self,n):
#         print(n)
#         self.print2(2)
    
#     def print2(self,n):
#         print(n)
#         self.print3(3)
#     def print3(self,n):
#         print(n)
#         self.print4(4)
#     def print4(self,n):
#         print(n)
#         self.print5(5)
#     def print5(self,n):
#         print(n)
    
# l1= Numbers()
# l1.print1(1)


# recursive way 
# def show(n):
#     if n>5:   # base condition: where the recursion will stop
#         return  # no base condition will give "stackoverflow error["
#     print(n)
#     show(n+1)
# show(1)


# find nth fibonacii number
# def fibonacii(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibonacii(n-1) + fibonacii(n-2)

# print(fibonacii(9))


# fibonacii using DP
# def fibonacii(n):
#     fib= [0,1]   # base case value are stored initially in the array
#     for i in range(2, n+1):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib[n]

# print(fibonacii(9))


# binary search using recusrsion
# def BinarySearch(arr,key,start,end):
#     mid= start + (end-start)//2
#     while(start<=end):
#         if arr[mid]== key:
#             return mid
#         elif arr[mid]>key:
#             return BinarySearch(arr,key,start,mid-1)
#         else:
#             return BinarySearch(arr,key,mid+1,end)
#     return -1

# arr= [2,4,5,7,9,10,15,22]
# print(BinarySearch(arr,5,0,len(arr)-1))


# sum of 1st n natural number: By recursion
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum(n-1)

# print(sum(5))


#linear search using Recursion  # will not work if ele is repeated
# def LinearSearch(arr,target,index):  # index tells from where we have to search
#     if index== len(arr): # means ele is not present as we have traversed the whole array
#         return -1
#     elif arr[index]== target:
#         return index
#     else:
#         return LinearSearch(arr,target,index+1)
    
# arr= [2,4,5,7,9,10,15,22]
# print(LinearSearch(arr,15,0))


# in binary search return a list containing all the index of the target ele
# indexes= []
# def LinearSearch(arr,target,index):  # index tells from where we have to search
#     if index== len(arr): # means ele is not present as we have traversed the whole array
#         pass
#     elif arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
#         indexes.append(index)  
#         LinearSearch(arr,target,index+1)
#     else:
#         LinearSearch(arr,target,index+1)
#     if indexes==[]: # if ele is not present
#         return -1
#     else:
#         return indexes
    
# arr= [2,4,5,7,4,9,4,10,15,22,4]
# print(LinearSearch(arr,4,0))
# # print(LinearSearch(arr,18,0))


# Q: in binary search return a list containing all the index of the target ele
# method2(better one) if you dont want to create a list outside function to store the indices
# in this you have to pass the index array as parameter
# variable passed as parameter has scope in all the function calls
# and variable declared inside the function has scope only within that function

# def LinearSearch(arr,target,index,list1):  # index tells from where we have to search
#     if index== len(arr): # as we have traversed the whole array
#         return list1
#     if arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
#         list1.append(index) 
#     # LinearSearch(arr,target,index+1,list1) # this will print 'None' as we are not returning
#                                                     # anything back to the previous called function
#     return LinearSearch(arr,target,index+1,list1) # search for next indices   
# arr= [2,4,5,7,4,9,4,10,15,22,4]
# indexes= []
# print(LinearSearch(arr,4,0,indexes))
# print(LinearSearch(arr,18,0,indexes))


# other method of above Q
# def LinearSearch(arr,target,index,list1):  # index tells from where we have to search
#     if index== len(arr): # as we have traversed the whole array 
#         pass
#     elif arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
#         list1.append(index)  
#         LinearSearch(arr,target,index+1,list1) # search for next indices 
#     else:
#         LinearSearch(arr,target,index+1,list1) # search for next indices 
#     return list1

# arr= [2,4,5,7,4,9,4,10,15,22,4]
# indexes= []
# # print(LinearSearch(arr,4,0,indexes))
# print(LinearSearch(arr,18,0,indexes))


#Do the same above Q but dont take list as argument, make list inside the function body itself
# just for knowledge and concept
def LinearSearch(arr,target,index):  # index tells from where we have to search
    list1= []
    if index== len(arr): # as we have traversed the whole array 
        pass
    elif arr[index]== target: # if ele is found add the index into the list and also
                              # add the list returned by the further function calls
        list1.append(index)  
        c= LinearSearch(arr,target,index+1)  # store the list returned to add with the previous list 
        list1= list1+ c   # will comtain all the index of target element till now

        # list1.append(index)      # writing this and next onen below lines as combination not giving 
        #                         #correct output 
        # list1+ LinearSearch(arr,target,index+1)  # list returned by the next function is not getting added
                                                # as after returning the value it will execute the further lines
                                                # or any statement ahead and we are adding in the same line when when we are calling

        # list1.append()+ LinearSearch(arr,target,index+1)   # writing only this giving None(None+list)

    else:
        return LinearSearch(arr,target,index+1)
    return list1

arr= [2,4,5,7,4,9,4,10,15,22,4]
print(LinearSearch(arr,4,0))
# print(LinearSearch(arr,18,0))




