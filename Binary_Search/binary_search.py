# this won't work properly if searching element is present more than one
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while(low<= up):
        mid= low+ (up-low)//2
        if arr[mid]== key:
           print("element is present at index: ",mid)
           break
        elif(arr[mid]> key):
            up= mid-1
        elif(arr[mid]<key):
            low= mid+1
        else:
            print("element is not present")



# recursive way
# def binary_search(arr,key,low,up):
#     if(up>= low):
#         mid= int(low+ (up-low)/2)
#         if arr[mid]== key:
#             print("element is present at index: ",mid)
#         elif arr[mid]> key:
#             return binary_search(arr,key,low,mid-1)
#         else:
#             return binary_search(arr,key,mid+1,up)
#     else:
#         print("element is not present")        

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

key= int(input("enter the element to search: "))
binary_search(lst,key)    
    
    
        