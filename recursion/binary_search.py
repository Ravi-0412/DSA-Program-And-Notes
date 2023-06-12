# binary search using recursion
def BinarySearch(arr,key,start,end):
    if start> end:
        return -1
    mid= start + (end-start)//2
    if arr[mid]== key:
        return mid
    if arr[mid]>key:
        return BinarySearch(arr,key,start,mid-1)
    return BinarySearch(arr,key,mid+1,end)

arr= [2,4,5,7,9,10,15,22]
print(BinarySearch(arr,11,0,len(arr)-1))