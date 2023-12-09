# Pivot_index of 'num'(pivot) means aisa index say 'j' find karna h 
# i) jiske bad i.e ele on right side of j' i.e from 'j+1' to 'n-1' is  >= num and
# ii) left side 'i' ele is <= pivot.
# then num ko 'j' pe rakh de to 'num' sort jo jaye i.e left me <= and right me >=.

# Note: But case me equal_to(=) condition lagayenge tb galat ho jayega. Isliye kisi ek case me lagana h.


def partition(arr,low,up):
    i, j= low, up
    pivot = arr[low]
    while i < j:
        # 1) for getting all ele on right > pivot. Find 1st index where arr[j] <= pivot.
        # increment 'i' until you find any element <= pivot
        while arr[j] > pivot:
            j-= 1
        # 2) for getting all ele on left  <= pivot. Find 1st index where arr[i] > pivot.
        # increment 'i' until you find any element greater than pivot
        while i < j and arr[i] <= pivot: 
            i+= 1
        if i < j:
            # Bringing smaller ele to left and bigger ele to right.
            arr[i], arr[j]= arr[j], arr[i]
    #wherever this condition fails means we have found 
	# the proper position of pivot and 'j' will give that
    # now,swap a[j] with pivot for proper position of pivot element

    # arr[j], pivot= pivot, arr[j]  # this will give incorrect output because you are just swapping the
                                    # arr[j] with value of pivot, not inside the array
                                    # but you have to change with element at pivot index then 
                                    #only it will get swapped inside the array
    arr[j], arr[low]= arr[low], arr[j]
    # after this pivot element will be get sorted
    # 'j' returns the proper index of pivot element i.e
	# all the elements on the left side of this index value 
	# will be smaller than the pivot element and all
	# the elements on the right side will be greater than pivot element
    return j

def quick_sort(arr,low,up):
    if(low < up):  # checking if there is more than one element.
        q= partition(arr,low,up)
        quick_sort(arr,0,q-1)
        quick_sort(arr,q+1,up)






