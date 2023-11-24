# def Rand(start, end, num):
#     res = []

#     for j in range(num):
#         res.append(random.randint(start, end))

#     return res

# # Driver Code
# num = 10
# start = 20
# end = 40
# print(Rand(start, end, num))  # (start, end): Range, num: how many times we want random number.

# Logic: rand7() -> rand49() -> rand40() -> rand10()
# Time: O(49/40) = the probabilty of exiting the loop i.e = 40/49

# Note vvi: Have to analyse the function of rand7() for each rand10() from 'lee' solution.

class Solution:
    def rand10(self):
        result = 40
        while result >= 40:
            result = 7 * (rand7() -1) + rand7() -1
        return result % 10 + 1


# This will also work . 
# Just stop at any multiple of '10' or for which you want to implement.

# Note: But when we stop at bigger multiple then time complexity will be less because 
# we can reach bigger multiple early.

# Time: O(49/10) = the probabilty of exiting the loop

class Solution:
    def rand10(self):
        result = 10
        while result >= 10:
            result = 7 * (rand7() -1) + (rand7() -1)
        return result % 10 + 1


# Some more examples:
# 1) Implement rand11() using rand3()

# logic: rand3() -> rand27() -> rand22 -> rand11

class Solution:
    def rand10(self):
        result = 22
        while result >= 22:
            result = 3*3* (rand3() -1) + 3* (rand3() -1) + (rand3() -1)
        return result % 11 + 1


# (2) Implement rand9() using rand7():

# lOGIC: rand7() -> rand49() -> rand45() -> rand9()
# Time Comlexity: O(49/45)

class Solution:
    def rand10(self):
        result = 45
        while result >= 45:
            result = 7 * (rand7() -1) + rand7() -1
        return result % 7 + 1


# 3) rand13() using rand6()

# Idea: rand6() -> rand36() -> rand26 -> rand13()

# Time Comlexity: O(36/26)

class Solution:
    def rand10(self):
        result = 36
        while result >= 36:
            result = 7 * (rand6() -1) + rand6() -1
        return result % 13 + 1


# 4) rand7() using rand5()
# Idea: rand5() -> rand25() -> rand21 -> rand7()

# Time Comlexity: O(36/26)

class Solution:
    def rand10(self):
        result = 21
        while result >= 21:
            result = 7 * (rand6() -1) + rand6() -1
        return result % 7 + 1
