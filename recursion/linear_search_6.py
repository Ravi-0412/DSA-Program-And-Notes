# linear search using Recursion  # will not work if ele is repeated
def LinearSearch1(arr,target,index):  # index tells from where we have to search
    if index== len(arr): # means ele is not present as we have traversed the whole array
        return -1
    if arr[index]== target:
        return index
    else:
        return LinearSearch1(arr,target,index+1)

arr= [2,4,5,7,9,10,15,22]
# print(LinearSearch1(arr,15,0))


# in linear search return a list containing all the index of the target ele
indexes= []
def LinearSearch2(arr,target,index):  # index tells from where we have to search
    if index== len(arr):
        if indexes== []:  # means ele is not present 
            return -1
        else:  # means ele is present
            return indexes
    if arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
        indexes.append(index)  
    return LinearSearch2(arr,target,index+1)
    
arr= [2,4,5,7,4,9,4,10,15,22,4]
# print(LinearSearch2(arr,4,0))
# print(LinearSearch2(arr,18,0))


# Q: in linear search return a list containing all the index of the target ele
# method2(better one): if you dont want to create a list outside function to store the indices
# in this you have to pass the index array as parameter
# variable passed as parameter has scope in all the function calls
# and variable declared inside the function has scope only within that function

def LinearSearch3(arr,target,index,list1):  # index tells from where we have to search
    if index== len(arr): # as we have traversed the whole array
        return list1
    if arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
        list1.append(index) 
    # LinearSearch3(arr,target,index+1,list1) # this will print 'None' as we are not returning
                                                    # anything back to the previous called function
    return LinearSearch3(arr,target,index+1,list1) # search for next indices   
arr= [2,4,5,7,4,9,4,10,15,22,4]
indexes= []
# print(LinearSearch3(arr,4,0,indexes))
# print(LinearSearch3(arr,18,0,indexes))


# other method of above Q
def LinearSearch4(arr,target,index,list1):  # index tells from where we have to search
    if index== len(arr): # as we have traversed the whole array 
        pass
    elif arr[index]== target: # if ele is found add in the list and again seasrch for further indexes
        list1.append(index)  
        LinearSearch4(arr,target,index+1,list1) # search for next indices 
    else:
        LinearSearch4(arr,target,index+1,list1) # search for next indices 
    return list1

arr= [2,4,5,7,4,9,4,10,15,22,4]
indexes= []
# # print(LinearSearch(arr,4,0,indexes))
# print(LinearSearch(arr,18,0,indexes))


#Do the same above Q but dont take list as argument, make list inside the function body itself
# just for knowledge and concept

def LinearSearch5(arr,target,index):  # index tells from where we have to search
    list1= []
    if index== len(arr): # as we have traversed the whole array 
        pass
    elif arr[index]== target: # if ele is found add the index into the list and also
                              # add the list returned by the further function calls
        list1.append(index)  
        c= LinearSearch5(arr,target,index+1)  # store the list returned to add with the previous list 
        list1= list1+ c   # will comtain all the index of target element till now

        # list1.append(index)      # writing this and next onen below lines as combination not giving 
                                 #correct output 
        # list1+ LinearSearch(arr,target,index+1)  # list returned by the next function is not getting added
                                                # as after returning the value it will execute the further lines
                                                # or any statement ahead and we are adding in the same line when when we are calling

        # list1.append()+ LinearSearch(arr,target,index+1)   # writing only this giving None(None+list)

    else:
        return LinearSearch5(arr,target,index+1)
    return list1

arr= [2,4,5,7,4,9,4,10,15,22,4]
print(LinearSearch5(arr,4,0))
# print(LinearSearch5(arr,18,0))


def search(arr,target,index):
    ans= []
    if index >= len(arr): 
        return ans
    if arr[index] == target:
        ans.append(index)
    smallAns = search(arr,target,index+1)
    return ans + smallAns 
arr= [2,4,5,7,4,9,4,10,15,22,4]
# print(search(arr,4,0))
