# Method 1:

# My mistake: I was inserting all nodes first then was calculating the pairs.
# In this pair will get repeated .

# So first count the pair possible for current number then insert.

# Read these two links to understand proeprly . After that we can find the shorter form(our solution).
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/solutions/1120320/c-clear-explanation-of-trie-tree-solution/
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/solutions/1122495/c-with-picture/


class Trie:
    def __init__(self):
        self.root= {}
    
    # will insert in binary from leftmost side and each num is stored in '32' bit binary.
    # Will keep one varible 'cnt' inside each node to count the number of ele that goes through that node.
    # initialise '{}' with cnt= 0 whenever you are making any new node.
    def insert(self, num):
        cur= self.root
        for i in range(31, -1, -1):
            bit= (num>> i) & 1   # getting the bit at 'i'th position.
            if bit not in cur:
                cur[bit]= {"cnt" :0} 
            cur= cur[bit]
            cur["cnt"] += 1

    # will count the pair with num having xor < k(strictly less than k)
    def countLess(self, num , k):
        count= 0
        cur= self.root
        for i in range(31, -1, -1):
            if not cur:
                break
            bit= (num>> i) & 1  # getting the 'i'th bit from left side for 'num'
            cmp = (k>> i) & 1 # getting the 'i'th bit from left side for 'val'
            # Which side we have to move and what all numbers we have to add will depend on 'cmp'
            # 1) if 'cmp' == 1
            if cmp == 1:
                # for getting less other no should have same bit as cur number
                # Then xor pair will be less than '1' i.e '0' for this bit.
                # i.e all number which will be same bit as cur number will contribute to ans
                # add all those numbers which has same bit as 'num'
                if cur.get(bit):
                    count += cur[bit]["cnt"]
                # Now for finding more possible numbers, will move in other direction(1-bit)  as 
                # for cmp ==1 , we will get more numbers in this direction only
                cur= cur.get(1 - bit , {})  # if '1-bit' is there then move to that direction else make cur ={}     
            else:
                # Here we can't add all numbers like above as that will not guarantee strictly lesser number
                # so will continue moving in same direction of 'bit'.
                # Because cmp= 0 so no way we can get pair xor < 0.
                cur= cur.get(bit , {})
        return count

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie= Trie()
        # for num in nums:
        #     trie.insert(num)

        ans= 0
        for num in nums:
            # count pair of cur 'num' with all the numbers before it.
            ans += trie.countLess(num, high + 1) - trie.countLess(num, low)
            trie.insert(num)  # After that insert cur 'num'.
        return ans


