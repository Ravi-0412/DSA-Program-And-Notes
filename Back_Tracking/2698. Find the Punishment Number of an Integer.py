# logic: 1) Find the square of each number from '1' to 'n'. square= i*i
# 2) we have to check whether we can "partitioned square into contiguous substrings such that 
# the sum of the integer values of these substrings equals i."

# for checking the partition possible: split from each remainining index using recursion.
# Time= O(n^2), n= len(square)

# why Brute force is getting accepted?
# Reason: Max value of n= 1000, max_value_of_square= 1000000  (7 digit).
# time: O(7^2)

# total time complexity: O(49 * n)


class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partitionPossible(num, i, res):
            if num== '':
                return i== res  # will return True if i==res else False
            # Try to partition into contiguos substring from each index
            for j in range(1, len(num) + 1):
                if partitionPossible(num[j: ], i, res + int(num[: j])):
                    # If any of the partition return True, then return True
                    return True
            # no such partition possible
            return False

        ans= 0
        for i in range(1, n +1):
            square= i * i
            if partitionPossible(str(square), i, 0):
                ans+= square
        return ans


# My mistake:
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partitionPossible(num, i):
            if num== '':
                return False
            # Try to partition into contiguos substring from each index
            for j in range(1, len(num) + 1):
                if int(num[: j]) + partitionPossible(num[j: ], i):   # if true then that will get added with '1' increasing the value.
                    # If any of the partition return True, then return True
                    return True
            # no such partition possible
            return False

        ans= 0
        for i in range(1, n +1):
            square= i * i
            if partitionPossible(str(square), i):
                ans+= square
        return ans