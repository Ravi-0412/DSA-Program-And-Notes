# Method 1: 
# very simple and easy. Just same as we do on pen and paper by taking choices for each boxes.
# logic: hmko 'len(arr)' no of boxes fill karna jo array me h wahi sb ele se.
#  remaining position ke liye koi bhi ele le sakte h and kisi ele ko choose karne ke bad
# usko aage nhi le sakte remaining boxes ko fill karne ke liye.
# isi tarah mera smaller subproblem generate hoga.

# in short vvi: At any time remaining position to fill will be equal to len(arr) and
# we can fill those positions one by one using elements of array.

# time: O(n! * n)  # n! = no of permutation and n= copying each permuatation
# space: n!

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []
        def permutation(arr, per):
            if not arr: 
                # means we have found the ans. Filled all the req places.
                ans.append(per)
                return
            # we can choose any number to fill the next position from remaining arr
            for i in range(len(arr)):  
                # us ele ko lene ke bad usko aage me include nhi kar sakte. so removing the added ele from arr and adding that to our one of permutation.
                permutation(arr[: i] + arr[i+1: ], per + [arr[i]])   
        
        permutation(nums, [])
        return ans

# Method 2: 
# To avoid copying the array after excluding the current included ele we can use set to check whether that has been added to 'per' or not.
# trying to fill remaining with all the ele if that ele is not used yet in that permutation.
# Since only distinct ele it will work fine when we will check the ele value.

# This is the most optimised among all because all other methods involve slicing.

# Not evvi: This logic will help in avoiding duplicate also i.e Q: "47. Permutations II".

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(per):
            if len(per) == len(nums):
                ans.append(per)
                return
            for i in range(len(nums)):
                if nums[i] not in included:
                    included.add(nums[i])
                    permutation(per + [nums[i]])
                    included.remove(nums[i]) 

        n = len(nums)   
        ans = []
        included = set()
        permutation([])
        return ans


# Note vvi: Pushing and poping in separate line in 'per' is making ans = []
# Reason: removing element from 'per' while backtrack is also removing ele from 'ans' and finally
# answer is getting = [].

# note vvi: 1) So avoid adding / poping in separate line in python specially with lists.
# Just add while calling function, it will get automatically get poped while backtrack and won't modify any related data structure.

# 2) or while adding into ans , add copy to avoid this scenario.
# 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(per):
            if len(per) == len(nums):
                # ans.append(per)   # this will give empty ans
                ans.append(per.copy())   # this will give correct ans
                return
            for i in range(len(nums)):
                if nums[i] not in included:
                    included.add(nums[i])   
                    per.append(nums[i])   # this one 
                    permutation(per)
                    # while backtracking remove arr[i]
                    included.remove(nums[i])   # and this one
                    per.remove(nums[i])    

        n = len(nums)   
        ans = []
        included = set()
        permutation([])
        return ans


# method 3:

# logic: just we are putting the upcoming letter(1st letter in remaining array) at all the gap formed by
# the already stored letter in answer.
# if there is say 'n' letter in ans then there will be 'n+1' gaps to fill the upcoming letter.
# and 1st gap will start from before zero itself and last gap will be at last.

# time and space same as above

# this will not remove duplicates as we are not checking 
# anything before filling we are just filling all the possible gaps

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
        def permutation(given , per):
            if not given: # if given string is empty 
                ans.append(per)
                return
            ch = given[0]   # upcoming char i.e 1st letter of remaining array
            # run a loop to call function again and again to put at diff positions
            for i in range(len(per)+1):    # filling the cur ele at 'i'th space.
                left = per[0:i]           # after this substring will put the 'ch'
                right = per[i:]           # and before this
                # after putting that char at one possible gap, call the function to fill the next char at new available position
                permutation(given[1:], left + [ch] + right)

        ans = []
        permutation(nums, [])
        return ans


# taking the ans list inside the function only.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums,[])
        
    def helper(self, nums, per):   
        ans= []
        if not nums:
            ans.append(per)
            return ans
        ch= [nums[0]]    
        for i in range(len(per)+1):
            left,right= per[:i], per[i:]
            ans += self.helper(nums[1:], left + ch+ right)   
        return ans



# count the no of total possible permutations
# just same as above ,only return count instead of returning 'ans'
def permutations(given, ans):
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



# Java
"""
// method 2:

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Set<Integer> included = new HashSet<>();
        
        // Start the permutation process
        permutation(new ArrayList<>(), nums, included, ans);
        
        return ans;
    }
    
    private void permutation(List<Integer> per, int[] nums, Set<Integer> included, List<List<Integer>> ans) {
        if (per.size() == nums.length) {
            // If the current permutation has the same length as nums, add it to the results
            ans.add(new ArrayList<>(per));
            return;
        }
        
        // Try adding each number in nums to the current permutation if it's not already included
        for (int i = 0; i < nums.length; i++) {
            if (!included.contains(nums[i])) {
                included.add(nums[i]);    // Mark the number as included
                per.add(nums[i]);         // Add the number to the current permutation
                
                permutation(per, nums, included, ans); // Recurse with the updated permutation
                
                // Backtrack by removing the last added number
                included.remove(nums[i]);
                per.remove(per.size() - 1);
            }
        }
    }
} 

"""



