def merge_sort(arr,low,up):
    if(low<up): 
        mid= int(low+ (up-low)/2)
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,up)
        merge(arr,low,mid,up)

def merge(arr,low,mid,up):
    low1,up1,low2,up2= low,mid,mid+1,up
    b= []
    while(low1<= up1 and low2<= up2):
        if(arr[low1]<arr[low2]):
            b.append(arr[low1])
            low1+=1
        else:
            b.append(arr[low2])
            low2+=1
    while(low1<=up1):
        b.append(arr[low1])
        low1+=1
    while(low2<=up2):
        b.append(arr[low2])
        low2+=1
    j= low
    k= 0
    while(j<up):
        arr[j]= b[k]
        j+= 1
        k+= 1

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

merge_sort(lst,0,n-1)
print(lst)

    
        
        


