# method 1: just sort and store ele in set then in list.
# time: O(n)= space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_ele= sorted(list(set(nums)))
        print(distinct_ele)
        if len(nums)== 0: return 0
        ans= 1
        count= 1
        i= 0
        while (i +1) < len(distinct_ele):
            if distinct_ele[i+1]!= distinct_ele[i] + 1:
                # ans= max(ans, count)    # updating here will give the incorrect ans as when your ans lies at last
                #  e.g: [1,2,3,4] then our ans won't get updated singlee time.
                count= 1
            elif distinct_ele[i+1]== distinct_ele[i] + 1:
                count+= 1
                ans= max(count, ans)
            i+= 1
        return ans

# another wayy of writing
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_ele= sorted(list(set(nums)))
        print(distinct_ele)
        if len(nums)== 0: return 0
        ans= 1
        count= 1
        i= 0
        while (i +1) < len(distinct_ele):
            if distinct_ele[i+1]!= distinct_ele[i] + 1:
                ans= max(ans, count)
                count= 1
            elif distinct_ele[i+1]== distinct_ele[i] + 1:
                count+= 1
            i+= 1
        ans= max(ans, count)
        return ans
    

# method 2:
# time: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)   # can use hashmap also, in both we can search in O(1)
        ans= 0
        for n in numSet:
            # check if this no is start of the sequence
            if n-1 not in numSet: # means 'n' is the start of the sequence
                # calculate the longest sequence from 'n'
                long= 0
                while n + long in numSet:
                    long+= 1
                # now we have got the longest sequence acc to the 'n'
                ans= max(ans, long)
            # otherwise 'n' is simply part of a sequence so simply skip, they will automatically get included.
        return ans


# method 3: using DSU
# Logic: we will try to merge(union) a cur ele with its adjacent ele if already merged(present in hashamp).
# At alst we will return the largest size of distinct component.

class DSU:
    def __init__(self, n):
        self.parent= [i for i in range(n)]
        self.size=   [1 for i in range(n)]
    
    def findParent(self, n):
        if n== self.parent[n]:
            return n
        self.parent[n]= self.findParent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2= self.findParent(n1), self.findParent(n2)
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2
            self.size[p2]+= self.size[p1]
        else:
            self.parent[p2]= p1
            self.size[p1]+= self.size[p2]
    
    # find the size of the largest component (distinct parent)
    def getLongestSequence(self):
        maxSize= 1 # minimum can be '1'.
        for i in range(len(self.parent)):
            if i== self.parent[i]:  # means parent of one of the component.
                maxSize= max(maxSize, self.size[i])
        return maxSize


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums)
        dsu= DSU(n)
        # to avoid repetition we have to keep value of num and to do union we need index of already added ele.
        numToIndex= collections.defaultdict(int) # [num: index]
        for i, num in enumerate(nums):
            if num in numToIndex:  # means we have alreay added this to a component
                continue
            # Try to merge(union) 'num' with any of the adjacent number which is already included i.e 'num+1' and 'num-1'
            # we will do union with the index value.
            if num + 1 in numToIndex:
                dsu.union(i, numToIndex[num + 1])
            if num - 1 in numToIndex:
                dsu.union(i, numToIndex[num - 1])
            # Add this curr num in hashmap
            numToIndex[num]= i
        
        # return dsu.getLongestSequence() if nums else 0
        return max(dsu.size) if nums else 0  # shortcut



# my method mistake in 2nd method : correct only but giving TLE
# Reason of TLE: here we are checking for very ele and in above method if are only checking if that ele is the start of the sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum= set(nums)
        hashmap= collections.defaultdict(int)  # [num: seq_count]
        ans= 0
        for num in setNum:
            cur= num
            count= 1
            while cur +1  in setNum:
                if cur + 1 in hashmap:
                    count+= hashmap[cur+1]
                    break
                else:
                    count+= 1
                cur+= 1

            hashmap[num]= count
            ans= max(ans, count)
        return ans

