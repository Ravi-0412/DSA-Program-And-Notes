def counting_sort(arr):
    n= len(arr)
    max_ele= max(arr)
    count= [0]*(max_ele+1) # to store the count of no of occurences of each element
    result= [0]*n      # to store the result
    #1. To store the count of each element in the count array
    for num in arr:
        count[num]+= 1
    print("no of occurence of each element: ", count)
    # to calculate how many numbers are smaller than or equal to a given number 
    for i in range(1,len(count)):
        count[i]+= count[i-1]
    print("no of elements smaller than a given number: ", count)
    #for output array: find the index of each element of the original
    #array in count array and place the element in 'result' array
    i= n-1
    while i>=0:
        result[count[arr[i]]-1]= arr[i]
        count[arr[i]]-= 1
        i-= 1
    print("sorted array is: ", result)

    # or use this 
    # for i in range(n-1,-1,-1):
    #     result[count[arr[i]]-1]= arr[i]
    #     count[arr[i]]-= 1
    # print("sorted array is: ", result)
    
arr= [0,1,4,2,1,0,5,3,2,1,4,5,1,0,2,7]
# arr= [4,2,2,5,3,3,1]
counting_sort(arr)





