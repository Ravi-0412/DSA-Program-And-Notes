# logic: just we are putting the upcoming letter at all the gap formed by
# the already stored letter in answer.
# Time Complexity: O(n*n!) Note that there are n! permutations and it 
# requires O(n) time to print a permutation or put into any data structure 
# space: O(n!) for storing each of permutation.

# this will not remove duplicates as we are not checking 
# anything before filling we are just filling all the possible gaps
def permutations(given, ans):
    if not given: # if given string is empty
        print(ans)
        return
    ch= given[0]   # pick char one by one from gievn string and put at diff possible positions
    # run a loop to call function again and again to put at diff positions
    for i in range(len(ans)+1):    # if there is say 'n' letter in ans then
                                    # there will be 'n+1' gaps to fill the upcoming letter
                                    # and 1st gap will start from before zero itself and last gap will be at last.
        left= ans[0:i]           # after this substring will put the 'ch'
        right= ans[i:]    # and before this
        # after putting that char at one possible gap, call the function to fill the next char at new available position
        permutations(given[1:], left + ch + right)

# permutations("abc", "")
# permutations("abca", "")




# storing the results into a list
def permutations(given, ans):
    res= []
    if not given: # if given string is empty
        new_res= []   # to store the global ans
        new_res.append(ans)
        return new_res
    ch= given[0]   # pick char one by one from gievn string and put at diff possible positions
    # run a loop to call function again and again to put at diff positions
    for i in range(len(ans)+1):    # if there is say 'n' letter in ans then
                                    # there will be 'n+1' gaps to fill the upcoming letter
                                    # and 1st gap will start from before zero itself 
        left= ans[0:i]           # after this substring will put the 'ch'
        right= ans[i:len(ans)]    # and before this
        res+= permutations(given[1:], left + ch + right)  # immediate parent node of the recursion call
                                                          # will keep on adding all the local 'ans' after 
                                                          # child will return the 'local ans'
    return res
# print(permutations("abc", "")) 
# print(permutations("aba", "")) 


# count the no of total possible permutations
# just same as above ,only return count instead of returning 'ans'
def permutations(given, ans):
    res= []
    count= 0
    if not given: # if given string is empty, then only we get one of the ans so incr count
        return 1     # simplest way of all the above three lines
    ch= given[0]   # pick char one by one from gievn string and put at diff possible positions
    # run a loop to call function again and again to put at diff positions
    for i in range(len(ans)+1):    # if there is say 'n' letter in ans then
                                    # there will be 'n+1' gaps to fill the upcoming letter
                                    # and 1st gap will start from before zero itself 
        left= ans[0:i]           # after this substring will put the 'ch'
        right= ans[i:len(ans)]    # and before this
        # res+= permutations(given[1:], left + ch + right)  # immediate parent node of the recursion call
                                                          # will keep on adding all the local 'ans'
        count+= permutations(given[1:], left + ch + right)        
    return count

# print(permutations("abc", "")) 
# print(permutations("abcd", "")) 
# print(permutations("aba", ""))  


# this i submitted on leetcode
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ans= []
#         self.helper(nums,[],ans)
#         return ans
#     def helper(self,nums,path,ans):   #p: processed(ans), up: unprocessed(actual input)
#         if not nums:
#             ans.append(path)
#             return
#         ch= [nums[0]]    # since we have to add each ele(char) with list
#         for i in range(len(path)+1):
#             left,right= path[:i], path[i:]
#             self.helper(nums[1:],left + ch+ right, ans)   


# method 2:
# another method and easy one
# for every position we have 'n' choices. 
# run a loop to check whether any ele has been added or not,for this 'n' choices.  for this take set 'included'
# if any ele not in included then add that ele to the ans else ignore
def permutations2(arr,ans,included):
    if len(ans)== len(arr):  # measn we have got one of the permutations
        print(ans)
        print(included, "set")
        return
    for i in range(len(arr)):
        if arr[i] not in included:
            included.add(arr[i])
            ans.append(arr[i])
            permutations2(arr,ans,included)
            # while backtracking remove arr[i]
            included.remove(arr[i]) 
            ans.remove(arr[i])

# arr= [1,2,3]
# included= set()  # will also conatain the permutation only.
# permutations2(arr,[],included)

# no need of included, we can check in 'ans'. but here time complexity will be more to check if arr[i] in 'ans' or not.
def permutations2(arr, ans):
    if len(ans)== len(arr):  # measn we have got one of the permutations
        print(ans)
        return
    for i in range(len(arr)):
        if arr[i] not in ans:
            ans.append(arr[i])
            permutations2(arr, ans)
            ans.pop()

arr= [1,2,3]
# permutations2(arr, [])


# method 3: just we fill the num at 'n' position while doing by pen and paper.
# logic: when we put any num in the ans then we skip that num in the original array.
# just the another way of writing the above logic.
# in this no need to check whether the curr num in the ans or not since we are skip the ele after adding into the ans.
# better one than above.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []
        self.dfs(nums,[],ans)
        return ans
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            # add nums[i] in the path and skip nums[i] from the original array.
            self.dfs(nums[:i] + nums[i+1: ], path + [nums[i]], res)


# method 4:
# Here no extra space
# logic: we are trying to bring every ele at every possible index by swapping and
#  when index== len(arr) means we have done required no of swap to get a ans.
def permutations3(ind,arr):
    if ind== len(arr):
        print(arr)
        return 
    for i in range(ind,len(arr)):
        arr[i],arr[ind]= arr[ind],arr[i]
        permutations3(i+1,arr)
        arr[i],arr[ind]= arr[ind],arr[i]

arr= [1,2,3]
permutations3(0,arr)


# method 5: 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
def permutations(str1,ans):
    if len(str1)==0:  # mens you have got one of the ans
        print(ans)
        return 1
    count= 0
    for i in range(len(str1)): 
        curr= str1[i]  # add one char to the 1st position one by one each
                       # and call the fun for the left string to fill the space
        left= str1[0:i] + str1[i+1:]  # will contain the remaining str 
                                      # excluding that we have added till now
                                      # i.e remove the string at ith index
        count+= permutations(left,ans+curr)   # agai call the call for the remaining string
    return count

# print(permutations("abc", ""))
# print(permutations("abcd", ""))


