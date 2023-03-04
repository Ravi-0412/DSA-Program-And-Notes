# length of LIS

def LIS(arr):
    n= len(arr)
    LIS= [1]*n
    for i in range(n):
        for j in range(i):
            if arr[i]> arr[j]:
                LIS[i]= max(LIS[i], 1+ LIS[j])
    return max(LIS)

# a = [ 3, 10, 2, 1, 20 ]
a = [10, 22, 9, 33, 21, 50, 41, 60]
# print(LIS(a))


# now for printing LIS
# this will give one of the possible LIS
# time:O(n^2)
def PrintLIS(arr):
    n= len(arr)
    LIS= [1]*n  # LIS[i] indicates that LIS that end at index 'i' from start. for each index at least ele at curr index will be get included so initialised with '1'
    pre_included_ind= [i for i in range(n)]  # will store the index of pre_included element in LIS
    for i in range(n):
        for j in range(i):
            if arr[i]> arr[j] and LIS[i]< 1+ LIS[j]:   # here we will have to write both the condition together. since we have to traverse back also. 
                # That's why we will only update the pre_included_ind when we will find any better ans.
                LIS[i]= 1+ LIS[j]
                # we get larger value so update pre_inc_ind for 'i' to find the next index with greater LIS 
                pre_included_ind[i]= j   # we included 'i' in LIS after ele 'j'.
   
    # now traverse back from the index with max LIS till you reach pre_ind become same because when it will matxh means LIS has started from here only
    # this will store the ans in reverse order
    print(LIS)
    ans= []
    start= LIS.index(max(LIS))  # starting in reverse order
    ans.append(arr[start])
    while start!= pre_included_ind[start]:
        start= pre_included_ind[start]
        ans.append(arr[start])
      
    print("length of LIS: ", max(LIS))
    print("one of the LIS is: ", ans[::-1])

# a = [ 3, 10, 2, 1, 20 ]
# a= [5,4,11,1,16,8]
a = [10, 22, 9, 33, 21, 50, 41, 60]
# PrintLIS(a)


# method 2: vvi
# just same methos we used for finding LIS using binary search.
# just like we need parentand child to print path, here also doing the same thing.
# time: O(n*logn)
import bisect
def PrintLIS1(arr):
    sub= []
    subInd= []  # will store the index of ele in sub
    trace=[-1] *len(arr)   # will store the pre_ind after that the cur ele came in LIS.
    for i, x in enumerate(arr):
        if not sub or sub[-1] < x:
            if subInd:  # then only we can update the trace 
                trace[i]= subInd[-1]   # cur ele 'x' which is at index 'i' took pre ele at 'subInd[-1]
            sub.append(x)       # cur ele
            subInd.append(i)    # index of cur ele
        else:
            idx= bisect.bisect_left(sub, x)
            if idx > 0:  # here we can only update
                trace[i]= subInd[idx -1]
            sub[idx]= x
            subInd[idx]= i
    
    # now traverse back to print the path.
    # last LIS will be last ele in sub or ele at last index in subInd.
    path= []
    t= subInd[-1]
    while t >= 0:  # after including the 1st ele, it will become negative.
        path.append(arr[t])
        t= trace[t]  # traverse back
    return path[::-1]

# a = [ 3, 10, 2, 1, 20 ]
a= [5,4,11,1,16,8]
# a = [10, 22, 9, 33, 21, 50, 41, 60]
print(PrintLIS1(a))

