# for logic: see the Aditya Verma video and read the discussion link in the sheet.
# method 1: Recursive way

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1== s2:  # same string will be always a scramble string
            return True
        # if not not same, check whether both give same string when sorted. basically we are cecking for anargam.
        if sorted(s1)!= sorted(s2):
            return False
        # unequal length and when len== 1 cases will come under above two.
        n= len(s1)
        # now try to partition at after each index i.e from index 1
        for i in range(1, n):
            # if we get scramble string either by 'not swapping' or by 'swapping' then return True
            # if we don't swap the child of s1. then check whether left of 's1' is scramble with left of s2 and same for right part
            not_swapped= self.isScramble(s1[: i], s2[: i]) and self.isScramble(s1[i: ], s2[i: ])
            if not_swapped:
                return True
            
            # if in case when we don't swap and don't get the sramble string then, try to swap the child of s1.
            # in this case, check left of s1 with right of s2 and right of s1 with left of s2.
            # here left and right of s2 will be different in case of swapping.
            # right of s2= last ka i char , left of s2= remaining char from starting
            swapped= self.isScramble(s1[: i], s2[-i: ]) and self.isScramble(s1[i: ], s2[: -i])
            if swapped:
                return True
        return False

# for memoising this we will have to store True or False wrt to given string like we do for array.
# but for this using a hasmap with both string as a tuple(in key) will be easy. By indexing it will be very tough.

# you can also update the ans in base case before returning
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dic= {}
        return self.helper(s1, s2, dic)
    
    def helper(self, s1, s2, dic):
        if s1== s2:  # same string will be always a scramble string
            return True
        # if not not same, check whether both give same string when sorted. basically we are cecking for anargam.
        if sorted(s1)!= sorted(s2):
            return False
        if (s1, s2) in dic:   # just cheking whether we have already calculated the value for given set of string.
            return dic[(s1, s2)]
        
        # unequal length and when len== 1 cases will come under above two.
        n= len(s1)
        # now try to partition at after each index i.e from index 1
        for i in range(1, n):
            # if we get scramble string either by 'not swapping' or by 'swapping' then return True
            # if we don't swap the child of s1. then check whether left of 's1' is scramble with left of s2 and same for right part
            not_swapped= self.helper(s1[: i], s2[: i], dic) and self.helper(s1[i: ], s2[i: ], dic)
            if not_swapped:
                dic[(s1, s2)]= True
                return True
            
            # if in case when we don't swap and don't get the sramble string then, try to swap the child of s1.
            # in this case, check left of s1 with right of s2 and right of s1 with left of s2.
            # here left and right of s2 will be different in case of swapping.
            # right of s2= last ka i char , left of s2= remaining char from starting
            swapped= self.helper(s1[: i], s2[-i: ], dic) and self.helper(s1[i: ], s2[: -i], dic)
            if swapped:
                dic[(s1, s2)]= True
                return True
        # if neither 'not_swapped' or nor 'swapped' return True
        dic[(s1, s2)]= False
        return False


# Tabulation will do after whole basic dsa. will be very tough.
