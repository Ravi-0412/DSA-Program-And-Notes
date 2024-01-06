# quick_select is used to find the kth smallest or kth largest element 
# in the time: o(n^2) ,but worst case can be avoided by using a random pivot. so average: 0(n^2)
# here doing for kth largest element

# Logic: If pivot of an element is 'n-k' then this means this ele is our ans i.e kth largest ele.
# So just find the pivot and check if it is ans or not.
# If not then check which side our ans lie i.e either left side of pivot or right side of pivot and call quick_select on that side.

# Exactly same as quick sort.

# link: https://www.geeksforgeeks.org/quickselect-algorithm/

def quick_select(arr,low,high,k):
    if(low<=high):  # if arr contain at least one element
        q= partition(arr,low,high)
        if(q== n-k): # pivot index element is equal to 'k' from start
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

# arr = [ 10, 4, 5, 8, 6, 11, 26,10,10 ]
# arr = [3,2,3,1,2,4,5,5,6]
arr = [3,2,1,5,6,4]
n= len(arr)
k= 2
print("{}th largest element is ".format(k))
print(quick_select(arr, 0, n - 1, k))

