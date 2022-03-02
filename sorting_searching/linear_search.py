def linear_search(arr,key):
    n= len(arr)
    flag=0
    for i in range(n):
        if(arr[i]==key):
            print("element is present at index: ",i)
            flag=1
    if(flag==0):
        print("element is not present")
    

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

key= int(input("enter the element to search: "))
linear_search(lst,key)
