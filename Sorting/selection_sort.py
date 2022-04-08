def swap(arr,x,y):
    temp= arr[x]
    arr[x]= arr[y]
    arr[y]= temp

def selection_sort(arr):
    n= len(arr)
    for i in range(n-1):
        min_index= i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index= j
        swap(arr,min_index,i)

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

selection_sort(lst)
print(lst)

