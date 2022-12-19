def FindIndex(arr):
    i, found= 0, 0
    while True:
        if arr[2**i]<= 1<=arr[2**(i+1)]:
            found= 1
        if found== 1:
            return BinarySearch(arr, 1, 2**i, 2**(i+1)-1)
        else:
            i+= 1


def BinarySearch(arr,key,start,end):
    low, up= start, end
    while low<= up:
        mid= (low+up)//2
        if arr[mid]>= key:
            up= mid-1
        else:
            low= mid+1
    return low

arr = [0, 0, 0, 0, 0,0,1,1,1,1]
# arr=  [1, 1, 1, 1,, 1, 1]
print(FindIndex(arr))
    

