# quick_select is used to find the kth smallest or kth largest element 
# in the time: o(n)
# here doing for kth largest element
# link: https://www.geeksforgeeks.org/quickselect-algorithm/

def quick_select(arr,low,high,k):
    if(low<=high):  # if arr contain at least one element
        q= partition(arr,low,high)
        if(q== n-k): # pivot index element is equal to kth largest
            return arr[q]
        if(q> n-k):  # element lies on left side of pivot index
            return quick_select(arr,low,q-1,k)
        else:    # element lies on right side of pivot index
            return quick_select(arr,q+1,high,k)

def partition(arr,low,high):
    pivot= arr[low]
    i,j= low,high
    while(i<j):
        while(arr[j]> pivot):
            j-= 1
        while(i<j and arr[i]<=pivot):
            i+= 1
        if(i<j):
            arr[i], arr[j]= arr[j], arr[i]
    arr[j],arr[low]= arr[low], arr[j]
    return j

arr = [ 10, 4, 5, 8, 6, 11, 26,10,10 ]
n= len(arr)
k= 6
print("{}th largest element is ".format(k))
print(quick_select(arr, 0, n - 1, k))

