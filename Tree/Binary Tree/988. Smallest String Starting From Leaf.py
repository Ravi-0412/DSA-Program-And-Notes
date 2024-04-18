# Very good problem to keep in mind. Will help a lot in future.

# My mistake:
# I was doing using bottom up i.e: answer(root) = min(answer(left) + root.val, answer(right) + root.val)
# But it won't work because:
# At current node you may ignore either left or right part after comparison but
# the part you ignored can be better ans than the part you you returned at later node.

# In short,The problem here is :

# 'string X < string Y' doesn't guarantee 'X + a < Y + a', where a is a character. 
# e.g.: "ab" < "abab", but "abz" > "ababz"

# Like above example you will ignore 'abab' since it is bigger than 'ab' but later
# after adding 'z' , 'ababz' will become smaller than 'abz'.

# try exmaple:
# 1) [4,0,1,1]. ans should be : "bae" but it will give "ae".
# 2)  [25, 1, null, 0, 0, 1, null, null, null, 0].  expected answer is "ababz" but it will give "abz".

# Fore more visualisation go through: https://leetcode.com/problems/smallest-string-starting-from-leaf/solutions/244205/divide-and-conquer-technique-doesn-t-work-for-this-problem/?envType=daily-question&envId=2024-04-17


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return  ""
        l = self.smallestFromLeaf(root.left)
        r = self.smallestFromLeaf(root.right)
        smallest = ""
        if l + chr(root.val + 97) > r + chr(root.val + 97):
            smallest = r + chr(root.val + 97)
        else:
            smallest = l + chr(root.val + 97)
        return smallest


# So only way it to track the path till leaf and then compare

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = ""

        def dfs(root, s):
            if not root:
                return
            if root.left == None and root.right == None:
                new = chr(root.val + 97) + s
                if self.ans == "" or self.ans > new:
                    self.ans = new
                return
            dfs(root.left,  chr(root.val + 97) + s)  # adding cur char at 1st since we need to take string leaf to root.
            dfs(root.right, chr(root.val + 97) + s)
        
        dfs(root, "")
        return self.ans
