# method 1:
def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        temp= arr[i]
        j= i-1
        while(arr[j]>temp and j>=0):
                arr[j+1]= arr[j]
                j-= 1
        arr[j+1]= temp


# lst= []
# n= int(input("enter the number of elements \n")) 
# print("enter the elements")   
# for i in range(n):
#     ele= int(input())
#     lst.append(ele)

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
