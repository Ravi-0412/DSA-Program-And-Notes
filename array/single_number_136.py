#submitted on leetcode ,Time: o(n), space: o(n)
def singlenumber(nums):
    hashmap= {}
    for i in nums:
        if i not in hashmap:
            hashmap[i]= 1
        else:
            hashmap[i]+= 1
    for key,value in hashmap.items():
        if(value%2!=0):
            return key
            break;
    # return 0   #if many elements occur odd times or no elements occur odd times(for gfg)
nums = [4,1,2,1,2]
print(singlenumber(nums))



#2nd method: best one using XOR operation
# Time: o(n), space: o(1)

# def singlenumber(nums):
#     x1=0
#     for num in nums:
#         x1=x1^num
#     return x1



