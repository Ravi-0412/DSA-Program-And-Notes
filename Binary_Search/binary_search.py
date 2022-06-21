# this won't work properly if searching element is present more than one
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while(low<= up):
        mid= (low+up)//2
        if arr[mid]== key:
           print("element is present at index: ",mid)
           break
        elif(arr[mid]> key):
            up= mid-1
        elif(arr[mid]<key):
            low= mid+1
        else:
            print("element is not present")



# # for searching element is present more than one time
# def binary_search(arr,key):
#     n= len(arr)
#     low=0
#     up= n-1
#     mid1=0
#     temp= 0
#     # this will give the index of searching element
#     # it may or may not be the first index of searching element
#     # will depend on the position of mid index
#     while(low<= up):
#         mid= low+ (up-low)//2
#         if arr[mid]== key:
#            print("element is present at index: ",mid)
#            mid1= mid
#            temp= 1
#            break
#         elif(arr[mid]> key):
#             up= mid-1
#         else:
#             low= mid+1
#     if(temp==0):
#         print("element is not present")
#     else:
#         # to get all the index of searching element left of position we got in above iteration
#         k= mid1-1
#         while(k>= 0 and arr[k]==key):
#             print("element is present at index: ",k)
#             k-= 1
#         # to get all the index of searching element right of position we got in above iteration
#         p= mid1+1
#         while(p<= n-1 and arr[p]==key):
#             print("element is present at index: ",p)
#             p+= 1


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
    
    
        