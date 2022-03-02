# since we dont know the size so using binary search after finding 
# length is not a good approach
# but if we can find that target ele exist bw any two index
# then we can apply binary search bw those index
# so,now problem reduces to find the range in which the target ele exist
# for finding the range we can move in chunk like first size of 2
# then 4, then 8 ....
import math
def FindRange(arr,target):
    # starting with size of 2
    start= 0
    end= 1
    curr_size= (end-start) + 1
    while(arr[end]< target): # means target not lie in this range
                             # so now incr the range in pow of tw
        start= end + 1
        # double the size
        end+= curr_size*2   # end=end+ size*2
    # when while loop will fail means we have found the range
    # so now apply binary search in this range to find the position
    position= BinarySearch(arr,target,start,end)
    return position


def BinarySearch(arr,key,start,end):
    low= start
    up= end
    while(low<= up):
        mid= (low+up)//2
        if arr[mid]== key:
           return mid
        elif(arr[mid]> key):
            up= mid-1
        else:
            low= mid+1
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
position= FindRange(arr,10)
print("{} is present at index {}:".format(10,position))



