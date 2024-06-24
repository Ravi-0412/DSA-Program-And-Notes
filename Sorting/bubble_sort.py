# lst= []
# n= int(input("enter the number of elements \n"))
# print("enter the elements")
# for i in range(n):
#     ele= int(input())
#     lst.append(ele)

#This swap function will just change the value of x,y but will make no 
# difference in the array
# def swap(x,y):
#     temp= x
#     x= y
#     y= temp

# swap function to swap inside the arr. x and y are index of ele we want to swap 
def swap(arr,x,y):
    temp= arr[x]
    arr[x]= arr[y]
    arr[y]= temp


def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        already_sorted= 0
        for j in range(n-i-1):  # as till 'i'th pass, 'i' element is already sorted at last
            if arr[j]> arr[j+1]:
                swap(arr,j,j+1)
                # arr[j],arr[j+1]= arr[j+1],arr[j]
                already_sorted= 1
        if already_sorted== 0:
            break
    return arr

lst= []
n= int(input("enter the number of elements \n")) 
print("enter the elements")   
for i in range(n):
    ele= int(input())
    lst.append(ele)

bubble_sort(lst)
print(lst)


# Java
"""
class Solution {
    public void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    public int[] bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            boolean alreadySorted = true;
            for (int j = 0; j < n - i - 1; j++) { // as 'i' elements are already sorted at the end
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    alreadySorted = false;
                }
            }
            if (alreadySorted) {
                break;
            }
        }
        return arr;
    }
"""