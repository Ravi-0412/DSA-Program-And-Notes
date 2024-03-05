# it basically checking all the subsequences formed with their sum.
# valid for all cases.
# Note vvi: We always have choice to 'not include' and we can only include when arr[i] <= target(remaining_sum)

def PrintSubsequence2(arr,ans,k):
    if not arr:
        if sum(ans)==k:
            print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    PrintSubsequence2(arr[1:],ans+ [arr[0]],k)
    # if we don't include the current ele 
    PrintSubsequence2(arr[1:],ans,k)

# arr= [1,2,1]
# arr= [2,3,5]
# k= 8
# print("possible subsequences or subset is: ")
# PrintSubsequence2(arr,[],k)


# little modification of above code as when in array will be greater than 'k' then no need to find subsequence for that number.
# note: will be only valid if all number will be positive only.

def PrintSubsequence3(arr,ans,k):
    if k==0:
        print(ans)
        return
    if not arr:    # don't writing this will give the error: index out of bound
        return
    # if we include the current ele, then add arr[ind] into the ans but we only include if the curr ele value is less than sum.
    if arr[0]<=k:  # if folows this tehn include otherwise don't include
        PrintSubsequence3(arr[1: ],ans+ [arr[0]],k-arr[0])
    # if we don't include the current ele 
    PrintSubsequence3(arr[1:],ans,k)

# arr= [1,2,1]
# k=2
# print("possible subsequences or subset is: ")
# arr= [17, 18, 6, 11, 2, 4]
# k = 6
# arr= [2,3,6,7]
# k= 7
# arr= [2,3,5]
# k= 8
# PrintSubsequence3(arr,[],k)

# Q: To print any of the subsequence with sum= k
# print any subsequences with sum =K and stop.
# just we have to avoid the further recursion call once we get any ans.
# so we must notify our parent that ans has been already found. That's why have to use any variable or 
# we have  to add something in return function when we will find any ans.
# Here returing 'True' in case we find the ans. Once we will find any ans just return from there itself.

def PrintSubsequence4(arr,ans,k):
    if not arr:
        if sum(ans)==k:
            print(ans)
            return True
        return False
    # if we include the current ele, then add arr[ind] into the ans
    if(PrintSubsequence4(arr[1:],ans+ [arr[0]],k))== True:   # if we have found any sequence then simply return no need to call any other function
        return True
    # if we don't include the current ele 
    if(PrintSubsequence4(arr[1:],ans,k))== True:
        return True
    return False

arr= [2,1,2,1]
print("possible subsequences or subset is: ")
PrintSubsequence4(arr,[],2)
# arr= [17, 18, 6, 11, 2, 4]
# k = 6
# PrintSubsequence4(arr,[],k)

# Related Q:
# 1) 77. Combinations
# 2) 78. Subsets