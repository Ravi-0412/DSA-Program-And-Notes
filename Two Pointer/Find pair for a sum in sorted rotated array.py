# same logic as unsorted just little change in how we change the
# lower and starting index

# Time: O(n)

def pair_sum_rotated_sorted(arr,k):
    n= len(arr)
    for i in range(0,n):
        if arr[i]> arr[(i+1)%n]: # since minimum element can be at index '0'
            break
        # means largest element at index 'i' and
        # smallest index at (i+1)% n
        # since rotated so we have  to use % for corner index
    right= i
    left= (i+1)% n  # because i can the last index i.e: 'n-1'
    while(left!= right):
        if arr[left]+ arr[right]== k:
            return True
        elif arr[left]+ arr[right]< k: # incr the index for finding the 
                                       # next greater element after the current smaller ele
            left= (left+1)% n
        else:
            right= (right-1 + n) %n  # added '+n' since it can go negative 
                                    # so add +n will to make it positive and 
                                    # since rotated so adding '+n' will not make any difference
    return False

arr= [11,15,26,38,9,10]
sum1= 35
sum2= 45
sum3= 26
sum4= 23
sum5= 47
print(pair_sum_rotated_sorted(arr,sum1))
print(pair_sum_rotated_sorted(arr,sum2))
print(pair_sum_rotated_sorted(arr,sum3))
print(pair_sum_rotated_sorted(arr,sum4))
print(pair_sum_rotated_sorted(arr,sum5))

# method2: optimising the above code. find the pivot using binary search but overall time complexity will be same only
# time: O(logn + n)= O(n)
