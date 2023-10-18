# time= O(n)
# Method 1: 
# Logic: Make another array and put num in proper order
# After that copy these value in original arrays.

# Time = Space = O(n)

def Reorder(arr,indices):
    n = len(arr)
    temp = [0] * n;
    # arr[i] should be
        # present at index[i] index
    for i in range(0,n):
        temp[indices[i]] = arr[i]

    # Copy temp[] to arr[]
    for i in range(0,n):
        arr[i] = temp[i]
        indices[i] = i


# Method 2:

# space= O(1)

# logic: start checking from index '0', if ele is at its correct position then only proceed to next ele.
# otherwise keep on swapping ele to its proper index and "indexes" also.

def Reorder(arr, indices):
    n= len(arr)
    i= 0
    while i < n:
        # curr ele is not at proper position
        if indices[i] != i:
            # send the curr ele to its proper index by swapping and also swap indices to check for next ele.
            ind= indices[i]  # to this index curr ele 'i'th ele of array should go.
            arr[i], arr[ind]= arr[ind], arr[i]
            indices[i], indices[ind]= indices[ind], indices[i]
        # curr ele is at proper position, so simply move further to chekc for next ele.
        # incr 'i' only in this case, because after swapping the cur ele at 'i' may not be at its correct position.
        else:
            i+= 1
    print("final num arr is :", arr)
    print("final indices arr is :", indices)
    
    
# arr= [10, 11, 12]
# indices = [1, 0, 2]

# arr=     [50, 40, 70, 60, 90]
# indices = [3,  0,  4,  1,  2]

arr = [10, 20, 30, 40, 50]
indices = [3, 1, 4, 0, 2] 

print(Reorder(arr, indices))



# Method 2: 
# Logic: Make another array and put num in proper order
# After that copy these value in original arrays.

def reorder(arr,index, n):
    temp = [0] * n;
    # arr[i] should be
        # present at index[i] index
    for i in range(0,n):
        temp[index[i]] = arr[i]

    # Copy temp[] to arr[]
    for i in range(0,n):
        arr[i] = temp[i]
        index[i] = i