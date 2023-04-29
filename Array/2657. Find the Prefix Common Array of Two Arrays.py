# method 1: Brute force and simplest
# using python inbuilt function to find the common elements between two arrays or set etc..


# all three method is giving correct result.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n= len(A)
        ans= []
        for i in range(n-1):
            # find common ele in both arrays till index 'i'
            # k= len(list(set(A[:i +1]) & set(B[: i+1])))   # no need to put in list in again
            # k= len(set(A[:i +1]) & set(B[: i+1]))  
            # k= len([value for value in A[:i +1] if value in B[: i+1]])
            k= len(set(A[: i+1]).intersection(B[: i+1]))
            ans.append(k)
            
        ans.append(n)  # at last all will common only as both are permuation of each another
        return ans
    

# method 2: for interview
# Create frequency array which will store the running frequency of each integer in both the arrays together. 
# Since, they are permutations, the frequency of the each element will reach 2 at max at any point during the iterations.
# when freq of any ele will '2' then that ele is common in both the array in this case incr common by '1'.

# time: O(n)= space
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n= len(A)  # lenth of both array will be equal only since both are permutation of one-another.
        common= 0  # will store the common ele till index 'i'.
        freq= [0]*51  # maximum value of ele can be '50'.
        ans= [0]*n
        for i in range(n):
            freq[A[i]]+= 1
            if freq[A[i]]== 2:
                common+= 1
            freq[B[i]]+= 1
            if freq[B[i]]== 2:
                common+= 1
            ans[i]= common
            # Because we are moving in one direction the common elements
            # will not be changed infact the count will remain same or increase
            # but will never get reduced and hence at index 'i' the number of
            # common elements will be 'cmn' 
        return ans

