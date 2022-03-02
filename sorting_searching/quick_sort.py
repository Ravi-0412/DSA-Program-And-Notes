
def partition(arr,low,up):
    i, j= low, up
    pivot= arr[low]
    while(i<j):
        while(arr[j]>pivot):  # decrement 'j' until you find any element smaller than or equal to pivot
            j-= 1
        while(i<j and arr[i]<=pivot): #increment 'i' until you find any element greater than pivot
            i+= 1
        if(i<j):
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
    if(low<up):
        q= partition(arr,low,up)
        quick_sort(arr,0,q-1)
        quick_sort(arr,q+1,up)

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

quick_sort(lst,0,n-1)
print(lst)





