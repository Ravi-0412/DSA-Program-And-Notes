def PrintSubsequence2(arr,ans,k):
    # if not arr or sum(ans)==k:    # this will print all the subsequence
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

arr= [1,2,1]
print("possible subsequences or subset is: ")
# PrintSubsequence2(arr,[],2)


# little modification of above code as when in array will be greater than 'k' then no need to find subsequence for that number

def PrintSubsequence3(arr,ans,k):
    if k==0:
        print(ans)
        return
    if not arr:    # don't writing this will give the error: index out of bound
        return
    # if we include the current ele, then add arr[ind] into the ans
    if arr[0]<=k:  # if folows this tehn include otherwise don't include
        PrintSubsequence3(arr[1:],ans+ [arr[0]],k-arr[0])
    # if we don't include the current ele 
    PrintSubsequence3(arr[1:],ans,k)

arr= [1,2,1]
print("possible subsequences or subset is: ")
PrintSubsequence3(arr,[],2)