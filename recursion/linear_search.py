# linear search using Recursion  # will not work if ele is repeated
def LinearSearch1(arr,target,index):  # index tells from where we have to search
    if index== len(arr): # means ele is not present as we have traversed the whole array
        return -1
    if arr[index]== target:
        return index
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


#Do the same above Q but dont take list as argument, make list inside the function body itself
# just for knowledge and concept
# Better one

# better and concise than all other
def search(arr,target,index):
    ans= []
    if index >= len(arr): 
        return ans
    if arr[index] == target:
        ans.append(index)
    return ans + search(arr,target,index+1)
arr= [2,4,5,7,4,9,4,10,15,22,4]
print(search(arr,4,0))
