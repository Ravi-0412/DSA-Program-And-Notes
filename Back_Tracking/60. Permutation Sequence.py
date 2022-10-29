# Method 1: Store all the possible permutations in list and then sort the list and return list[k-1]
# correct only but giving TLE
# time: O(n!*n + n!logn!)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_arr= [str(i) for i in range(1,n+1)]
        ans, per= [], ""
        self.permutations(num_arr,ans, per)
        ans.sort()
        return ans[k-1]

    
    def permutations(self,arr,ans,per):
        if not arr:
            ans.append(per)
            return 
        for i in range(len(arr)):
            added_char= arr[i]
            remaining_char= arr[:i] + arr[i+1:]
            self.permutations(remaining_char,ans,per + added_char)


# optimised one: VVI
# write the thinking process and logic in detail
# Q with very good and very basic logic
# time= Space= O(n)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_arr= [str(i+1) for i in range(0,n)] # we have to return ans in string
        # ans= ""  # will print the empty string as string is immutable it can't be updated everywhere automatically like list once we will update anywhere
        ans= []
        self.permutations(num_arr,ans,n,k-1,0)   # using zero indexing so will find the 'k-1'th char
        return "".join(ans)   # converting into list

    def fact(self,n):  
        if n==1:
            return 1
        return n*self.fact(n-1)
    
    def permutations(self,arr,ans,n, remaining_k, no_added):
        if remaining_k== 0:
            ans+= arr
            return ans
        if no_added==n:
            return ans
        no_gen_by_each_char= self.fact(n-no_added -1)   # just fix one char and find no of permutation for remaining
        index_gen_char= remaining_k//no_gen_by_each_char 
        char_to_chose= arr[index_gen_char]
        ans.append(char_to_chose)
        remaining_k-= no_gen_by_each_char*index_gen_char
        arr.pop(index_gen_char)
        self.permutations(arr,ans,n, remaining_k, no_added+1)




# converting into iterative form, very good one. Do it later
