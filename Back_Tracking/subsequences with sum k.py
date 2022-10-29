def PrintSubsequence2(arr,ans,k):
    # if not arr or sum(ans)==k:    # this will print all the subsequence. my mistake
    #     print(ans)
    #     return

    if not arr:
        if sum(ans)==k:
            print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    
    # PrintSubsequence1(ind+1,arr,ans.append(arr[ind]),n)    # will give error as it will return the value of append which is None
    PrintSubsequence2(arr[1:],ans+ [arr[0]],k)
    # if we don't include the current ele 
    PrintSubsequence2(arr[1:],ans,k)

# arr= [1,2,1]
arr= [2,3,5]
k= 8
print("possible subsequences or subset is: ")
PrintSubsequence2(arr,[],k)



# little modification of above code as when in array will be greater than 'k' then no need to find subsequence for that number

def PrintSubsequence3(arr,ans,k):
    if k==0:
        print(ans)
        return
    if not arr:    # don't writing this will give the error: index out of bound
        return
    # if we include the current ele, then add arr[ind] into the ans
    if arr[0]<=k:  # if folows this tehn include otherwise don't include
        PrintSubsequence3(arr,ans+ [arr[0]],k-arr[0])
    # if we don't include the current ele 
    PrintSubsequence3(arr[1:],ans,k)

# arr= [1,2,1]
# k=2
# print("possible subsequences or subset is: ")
# arr= [17, 18, 6, 11, 2, 4]
# k = 6
# arr= [2,3,6,7]
# k= 7
arr= [2,3,5]
k= 8
# PrintSubsequence3(arr,[],k)




# print any subsequences with sum =K and stop
# just we have tp avoid the further recursion call once we get any ans
def PrintSubsequence4(arr,ans,k):
    if not arr:
        if sum(ans)==k:
            print(ans)
        return True
    # if we include the current ele, then add arr[ind] into the ans
    if(PrintSubsequence4(arr[1:],ans+ [arr[0]],k))== True:   # if we have found any sequence then simply return no need to call any other function
        return
    # if we don't include the current ele 
    if(PrintSubsequence4(arr[1:],ans,k))== True:
        return 
    return False    # if none of the above return then it means subsequence with that sum is not present

# arr= [1,2,1]
# print("possible subsequences or subset is: ")
# PrintSubsequence4(arr,[],2)
arr= [17, 18, 6, 11, 2, 4]
k = 6
# PrintSubsequence4(arr,[],k)


# count no of subsequences with sum= k
def PrintSubsequence5(arr,k):
    if k==0:
        return 1
    if not arr:    # don't writing this will give the error: index out of bound
        return 0
    count= 0
    # if we include the current ele, then add arr[ind] into the ans
    if arr[0]<=k:  # if folows this tehn include otherwise don't include
        count+= PrintSubsequence5(arr[1:],k-arr[0])
    # if we don't include the current ele 
    count+= PrintSubsequence5(arr[1:],k)
    return count

# arr= [1,2,1]
arr= [17, 18, 6, 11, 2, 4]
# print("No of subsequences with given sum is: ")
# print(PrintSubsequence5(arr,6))
