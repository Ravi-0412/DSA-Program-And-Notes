# logic: just we are putting the upcoming letter at all the gap formed by
# the already stored letter in answer
# Time Complexity: O(n*n!) Note that there are n! permutations and it 
# requires O(n) time to print a permutation.
def permutations(given, ans):
    if not given: # if given string is empty
        print(ans)
        return
    ch= given[0]   # pick char one by one from gievn string and put at diff possible positions
    # run a loop to call function again and again to put at diff positions
    for i in range(len(ans)+1):    # if there is say 'n' letter in ans then
                                    # there will be 'n+1' gaps to fill the upcoming letter
                                    # and 1st gap will start from before zero itself 
        left= ans[0:i]           # after this substring will put the 'ch'
        right= ans[i:len(ans)]    # and before this
        # after putting that char at one possible gap, call the function to fill the next char at new available position
        permutations(given[1:], left + ch + right)

# permutations("abc", "")
# permutations("abca", "")

# the above logic will not remove duplicates as we are not checking 
# anything before filling we are just filling all the possible gaps


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

print(permutations("abc", "")) 
print(permutations("abcd", "")) 
# print(permutations("aba", ""))  


# this i submitted on leetcode
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []
        self.helper(nums,[],ans)
        return ans
    def helper(self,nums,path,ans):   #p: processed(ans), up: unprocessed(actual input)
        if not nums:
            ans.append(path)
            return
        ch= [nums[0]]    # since we have to add each ele(char) with list
        for i in range(len(path)+1):
            left,right= path[:i], path[i:]
            self.helper(nums[1:],left + ch+ right, ans)   


# tried a lot by taking ans inside the function but was not able to do
# have to ask someone, how to do by this logic

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return self.helper([],nums)
#     def helper(self,p,up):   #p: processed(ans), up: unprocessed(actual input)
#         ans= [[]]
#         if not up:
#             new_ans= [p]
#             return new_ans
#         ch= [up[0]]
#         for i in range(len(p)+1):
#             left,right= p[:i], p[i:]
#             ans+= self.helper(left + ch+ right, up[1:])   # wrong will print many empty list also inside the ans
#         return ans

