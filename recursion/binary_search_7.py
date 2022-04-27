# binary search using recusrsion
def BinarySearch(arr,key,start,end):
    mid= start + (end-start)//2
    while(start<=end):
        if arr[mid]== key:
            return mid
        elif arr[mid]>key:
            return BinarySearch(arr,key,start,mid-1)
        else:
            return BinarySearch(arr,key,mid+1,end)
    return -1

arr= [2,4,5,7,9,10,15,22]
print(BinarySearch(arr,5,0,len(arr)-1))