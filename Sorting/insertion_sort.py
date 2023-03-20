# method 1:
def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        temp= arr[i]   # when we will shift the ele then ele at 'i' will change. so we have to store in temp variable.
        j= i-1
        while j>=0 and arr[j]>temp :  # until you find ele <= temp.
                arr[j+1]= arr[j]    # move one 'j' one position ahead to create the space for 'temp'.
                j-= 1
        arr[j+1]= temp    # 'j' will be pointing to index '<=' temp so we will put 'temp' at 'j+1'.


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
