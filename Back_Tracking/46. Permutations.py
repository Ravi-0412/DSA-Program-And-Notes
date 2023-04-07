# very simple and easy. Just same as we do on pen and paper by taking choices for each boxes.
# logic: hmko 'len(arr)' no of boxes fill karna jo array me h wahi sb ele se.
#  remaining position ke liye koi bhi ele le sakte h and kisi ele ko choose karne ke bad usko aage nhi le sakte remaining boxes ko fill karne ke liye.
# isi tarah mera smaller subproblem generate hoga.

# time: O(n! * n)  # n! = no of permutation and n= copying each permuatation
# space: n!
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans= []

        def permutation(arr, per):
            if not arr:  # means we have found the ans
                ans.append(per)
                return 
            for i in range(len(arr)):  # we can choose any number to fill remaining position i.e 'len(arr)'
                permutation(arr[: i] + arr[i+1: ], per + [arr[i]])   # us ele ko lene ke bad usko aage me include nhi kar sakte. so removing the added ele from arr.
        
        permutation(nums, [])
        return ans

# To avoid copying the array after excluding the current included ele we can use set to check whether that has been added to 'per' or not.
# trying to fill remaining with all the ele if that ele is not used yet in that permutation.
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


# method 2:

# logic: just we are putting the upcoming letter(1st letter in remaining array) at all the gap formed by
# the already stored letter in answer.
# if there is say 'n' letter in ans then there will be 'n+1' gaps to fill the upcoming letter.
# and 1st gap will start from before zero itself and last gap will be at last.

# time and space same as above

# this will not remove duplicates as we are not checking 
# anything before filling we are just filling all the possible gaps
def permutations(given, per):
    if not given: # if given string is empty 
        print(per)
        return
    ch= given[0]   # upcoming char i.e 1st letter of remaining array
    # run a loop to call function again and again to put at diff positions
    for i in range(len(per)+1):    # filling the cur ele at 'i'th space.
        left= per[0:i]           # after this substring will put the 'ch'
        right= per[i:]    # and before this
        # after putting that char at one possible gap, call the function to fill the next char at new available position
        permutations(given[1:], left + ch + right)

# permutations("abc", "")
# permutations("abca", "")


# taking the ans list inside the function only.
# this also submitted on leetcode
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
            ans+= self.helper(nums[1:], left + ch+ right)   
        return ans



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



