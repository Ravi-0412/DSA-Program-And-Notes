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
# Space= O(n), time= O(n^2) (every time we are poping so every time O(n) for shifting).

# logic: we are directly targeting the char from which we can get the ans by seeing the 'no of permutation we can form by fixing one char' and
# 'no left to go' and 'no left to add'.
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_arr= [str(i+1) for i in range(n)] # we have to return ans in string. num is from '1 to n'.
        # ans= ""  # will print the empty string as string is immutable it can't be updated everywhere automatically like list once we will update anywhere
        ans= []
        self.permutations(num_arr,ans,n,k-1,0)   # using zero indexing so will find the 'k-1'th char
        return "".join(ans)   # converting into list

    def fact(self,n):  
        if n==1:
            return 1
        return n*self.fact(n-1)
    
    def permutations(self,arr,ans,n, remaining_k, no_added):
        if remaining_k== 0:  # then all char present in arr should be added as it is i.e in same order
            ans+= arr
            return ans
        # if no_added==n:  # no need of this as it is not possible that remaining_k== 0 and no_added== n.
        #     return ans
        no_gen_by_each_char= self.fact(n- no_added -1)   # just fix one char and find no of permutation for remaining
                        # we are fixing each char(-1) and finding the no of permutation we can get by fixing this curr char.
        index_gen_char= remaining_k//no_gen_by_each_char  # next possible index we have to fix to get the ans.
        char_to_chose= arr[index_gen_char]              # next possible char we have to fix to get the ans
        ans.append(char_to_chose)  # chosing the char one by one that will form the ans
        remaining_k-= no_gen_by_each_char*index_gen_char   #  
        arr.pop(index_gen_char)  # pop the char that we have added into the ans.
        self.permutations(arr,ans,n, remaining_k, no_added+1)


# better one of above
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_arr= [str(i+1) for i in range(n)] # we have to return ans in string. num is from '1 to n'.
        # ans= ""  # will print the empty string as string is immutable it can't be updated everywhere automatically like list once we will update anywhere
        ans= []
        self.permutations(num_arr, ans, k-1)   # using zero indexing so will find the 'k-1'th char
        return "".join(ans)   # converting into list

    def fact(self,n):  
        if n==1:
            return 1
        return n*self.fact(n-1)
    
    def permutations(self, arr, ans, remaining_k):
        if remaining_k== 0:  
            ans+= arr
            return ans
        no_gen_by_each_char= self.fact(len(arr) -1)   # just fix one char and find no of permutation for remaining
                        # we are fixing each char(-1) and finding the no of permutation we can get by fixing this curr char.
        index_gen_char= remaining_k//no_gen_by_each_char  # next possible index we have to fix to get the ans.
        char_to_chose= arr[index_gen_char]              # next possible char we have to fix to get the ans
        ans.append(char_to_chose)  # chosing the char one by one that will form the ans
        remaining_k-= no_gen_by_each_char*index_gen_char   #  
        arr.pop(index_gen_char)
        self.permutations(arr,ans, remaining_k)


# converting into iterative form, very good one and easy one.
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_arr= [str(i+1) for i in range(n)] # we have to return ans in string. num is from '1 to n'.
        ans= []
        k= k- 1  # using indexing zero in arr
        while k!= 0:
            no_gen_by_each_char= self.fact(len(num_arr) -1)
            index_of_gen_char= k// no_gen_by_each_char
            char_to_chose= num_arr[index_of_gen_char]
            ans.append(char_to_chose)
            k-= index_of_gen_char *(no_gen_by_each_char)
            num_arr.pop(index_of_gen_char)
        # now it means only we have to add all char in arr to ans, to get the actual ans.
        ans+= num_arr
        return "".join(ans)

    def fact(self,n):  
        if n==1:
            return 1
        return n*self.fact(n-1)

# Note: If asked for 'Kth permutation' in any general(unsorted array), then just sort the array and do the same thing.
