# Logic : 1st find the range in whcih '1' lies
# Then find the position of 1st one in that range.

def FindIndex(arr):
    i= 0
    while(arr[2**(i+1)]< 1): # means target not lie in this range
                             # so now incr the range in pow of tw
        i+= 1
    # when while loop will fail means we have found the range
    # so now apply binary search in this range to find the position
    position= BinarySearch(arr, 1, 2**i -1, 2**(i+1))   # start= 2**i -1 to handle the case when ele is present at zero index.
    return position


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
arr=  [1, 1, 1, 1, 1, 1]
print(FindIndex(arr))
    

