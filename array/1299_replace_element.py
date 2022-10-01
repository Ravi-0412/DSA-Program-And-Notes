

# # 1st method(normal brute force): modified of 1st methode(commented lines)
# arr = [4,9,8,4,7]
# n= len(arr)
# k=0
# for num in arr[k:n-1]:
#     greatest= -1000000
#     j=k+1
#     while(j<=n-1):
#         if(arr[j]>=greatest):
#             greatest= arr[j]
#         j+= 1
#     arr[k]= greatest
#     k+= 1
# arr[n-1]= -1
# print(arr)

# # simple and straight foward brute force
# arr = [4,9,8,4,7]
# n= len(arr)
# for i in range(0,n-1):
#     greatest= -1000000
#     k= i+1
#     while(k<=n-1):
#         if(arr[k]>=greatest):
#             greatest=arr[k]
#         k+= 1
#     arr[i]= greatest
# arr[n-1]= -1
# print(arr)


# brute force but very concise and simple: Accepted 
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         n= len(arr)
#         for i in range(n-1):
#             arr[i]= max(arr[i+1:])
#         arr[n-1] = -1
#         return arr


# 2nd method- time: o(n), space= o(1)
# very better solution
# logic: tranverse from right to left and store the element with max_ele_seen_so_far
# comparing the element in max_seen_so_far
# max_seen_so_far will contain the maximum ele seen till now from right side
# and replace the iterating element with max_ele_seen_so_far as we are traversing from right to left

arr = [17,18,5,4,6,1]
n= len(arr)
max_ele_seen_so_far= arr[n-1]
arr[n-1]= -1
for i in range(n-2,-1,-1):
    temp=arr[i]  # to comapre arr[i] with max_ele_seen_so_far after updating arr[i]
    arr[i]= max_ele_seen_so_far
    if(temp>=max_ele_seen_so_far):
        max_ele_seen_so_far= temp
print(arr)



# another way of writing above code
# mostly same code and logic is totally same as "replacing by nextLargerElement in right" 
# just uncomment the three lines in the code 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        stack= [arr[n-1]] # will store the all the larger ele till index 'i'
        # since we have to compare with last ele so we pushed last ele into the stack

        ans= [-1]  # for last ele it will be '-1' only
        # traverse the array from right to left
        last_poped= 0  # will store the last poped ele
        for i in range(n-2,-1,-1):
            # run the loop till you get any ele greater than curr ele or stack becomes empty
            while(stack and stack[-1]<= arr[i]):
                    # stack.pop()    # only this was fine for 'nextgreater ele on right'
                    last_poped= stack.pop()
            if stack== []:  # since we are poping in above steps so we have to check for empty stack
                            # empty stack means either it is the largest ele till now
                            # so ans will be 'last_poped'
                ans.append(last_poped)
                # ans.append(-1)      # this was needed in case of 'next greater ele' as if there is no max ele ele on RHS return -1
                stack.append(arr[i])
            else:  # means stack top is greater than arr[i]
                ans.append(stack[-1])
                # stack.append(arr[i])  # uncomment this for nextgreater ele on right as the curr ele can be next greater for incoming ele

        # now reverse the ans to get the actual ans 
        return ans[::-1]


# another method: better one-concise way of above methods(stack one) (16/04/2022)
# just same logic as 2nd method 
# traverse from right to left and only store the maximum ele in the stack 
# i.e stack will contain only one ele always at any point and that ele will max till now from right side
# in this there no need of while loop since we have to compare the curr ele with only on ele(top one) on the stack
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)
        if n== 1:
            return [-1]
        stack, ans= [], []
        # initialise for last ele
        stack.append(arr[n-1])
        ans.append(-1)
        for i in range(n-2,-1,-1):
            # if arr[i]> stack measn arr[i] is the maximum ele on RHS till now
            # so just pop the stack top and append 'poped one' to the ans
            # poped will be the greatest for arr[i] and all the ele so far
            if arr[i]> stack[-1]:
                temp= stack.pop()
                ans.append(temp)
                # append arr[i] to the stack since arr[i] is the greatest till now
                stack.append(arr[i])
            else:  # means top of the stack is the greatest . so no need to append arr[i] in the stack
                ans.append(stack[-1])
        return ans[::-1]

