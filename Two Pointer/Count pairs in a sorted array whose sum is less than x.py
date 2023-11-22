# just apply two sum and when you find "sum< target" 
# then you can take start index ele with any of the ele from 'start+1' to 'end' all pair will give sum < target.
# So incr count= count + 'end- start' and update both start and end pointer.

# But it will also print duplicates.
# for avoiding duplicates, just move start pointer to next distinct ele like "15. sum".

def countPairs(arr, target):
    n= len(arr)
    count= 0
    start, end= 0, n-1
    while start< end:  
        if arr[start] + arr[end] >= target:
                # until you find sum < target.
                end-= 1
        else: # means < target
            count+= end- start
            start+= 1
            end-= 1
    return count


# arr= [1, 2, 3, 4, 5, 6, 7, 8]
arr= [1, 3, 7, 9, 10, 11]
target= 7
print(countPairs(arr, target))