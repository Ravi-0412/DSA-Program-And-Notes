# subsequences is same as subset except subset doesn't maintain the relative order
# but for subset also ans will be same only as (1,3) and (3,1) can't be in the subset as same time
# because subset doesn't allow duplicates
# subset: basically means taking any no of elements in any order

# time complexity= O(2^n *n), 2^n; total no fo subsequences and for each we traversing nearly the whole array
# space complexity= O(n), maximum recursion depth
# expanation in note, page no: 24

# this will print alll subset inside a list separately
# all subsequence are subset but reverse is not true
def PrintSubsequence(ind,arr,ans,n):
    if ind>= n:
        print(ans)
        return
    # if we include the current ele
    ans.append(arr[ind])
    PrintSubsequence(ind+1,arr,ans,n)

    # if we don't include the current ele then,we have to first remove the current ele
    #  as we have already added above and then call the function for next index
    ans.pop()
    PrintSubsequence(ind+1,arr,ans,n)

# arr= [1,2,3]
# ans= []
# print("possible subsequences or subset is: ")
# PrintSubsequence(0,arr,ans,3)


# another way of writing 
def PrintSubsequence1(ind,arr,ans,n):
    if ind>= n:
        print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    
    # PrintSubsequence1(ind+1,arr,ans.append(arr[ind]),n)    # will give error as it will return the value of append which is None
    PrintSubsequence1(ind+1,arr,ans+ [arr[ind]],n)
    # if we don't include the current ele 
    PrintSubsequence1(ind+1,arr,ans,n)

arr= [1,2,3]
ans= []
print("possible subsequences or subset is: ")
# PrintSubsequence1(0,arr,ans,3)

# another way of writing the above code
def PrintSubsequence2(arr,ans):
    if not arr:
        print(ans)
        return
    # if we include the current ele, then add arr[ind] into the ans
    PrintSubsequence2(arr[1:],ans+ [arr[0]])
    # if we don't include the current ele 
    PrintSubsequence2(arr[1:],ans)

arr= [1,2,1]
print("possible subsequences or subset is: ")
# PrintSubsequence2(arr,[])



