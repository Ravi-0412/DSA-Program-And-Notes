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
def PrintLIS(arr):
    n= len(arr)
    LIS= [1]*n  # LIS[i] indicates that LIS that end at index 'i' from start. for each index at least ele at curr index will be get included so initialised with '1'
    pre_included_ind= [i for i in range(n)]  # will store the index of pre_included index in LIS
    for i in range(n):
        for j in range(i):
            if arr[i]> arr[j] and LIS[i]< 1+ LIS[j]:
                LIS[i]= 1+ LIS[j]
                # we get larger value so update pre_inc_ind for 'i' to find the next index with greater LIS 
                pre_included_ind[i]= j
   
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

a = [ 3, 10, 2, 1, 20 ]
a= [5,4,11,1,16,8]
# a = [10, 22, 9, 33, 21, 50, 41, 60]
PrintLIS(a)