# observations: 
# 1) 2 letter words can be of 2 types:
# Where both letters are same
# Where both letters are different

# 2) only pairs like ('aa', 'aa') or ('ab', 'ba') can put on two sides respectively

# logic: while traversing the words if we there is palindrome of curr word already present
# then we can combine both of them to form a palindrome of 'length= 4'.
# put one word at leftmost side and one word at rightmost side of already formed palindrome.

# but there can be more than one same palindrome after combining so storing the freq of word also.
# e.g: [lc,lc, cl,cl]

# After forming the palindrome traversing whole array, we can add max one word having both character equal(palindromic word)
# we can keep this word in middle. This will increase the length of ans by '2'.
# we can include such one word at last.
# vvi: adding more than one such will not form a valid palindrome. 

# even no of duplicates pair will get cancelled forming palindrome. e.g: [gg, gg, gg], after operation we will left with : [gg] only one time.

# time: O(2*n)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq= collections.defaultdict(int)
        ans= 0
        for word in words:
            if word[::-1] in freq:
                ans+= 4
                freq[word[::-1]]-= 1  # one pair we have included into ans
                if freq[word[::-1]]== 0:  # delete we can't form new pair.
                    del freq[word[::-1]]
            else:  # only here we will add in hashmap . in above case directly got included to ans
                freq[word]= 1 + freq.get(word, 0)

        # Add any one palindromic word to the alrady formed palindrome.
        for s in freq.keys():
            if s== s[::-1]:
                ans+= 2
                break
        return ans