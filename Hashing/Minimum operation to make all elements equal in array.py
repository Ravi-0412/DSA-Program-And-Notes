# Note: we can add, subtract, multiply, divide by any number.

# logic: we can make all array equal in max 'n-1' operation if all ele will be distinct
# by addition or subtraction operation or any other operation.

# so if all ele are distinct , we will need 'n-1' operation no matter what ele we choose as target.

# Note vvi: if there are duplicates elements then for minimum no of operation we will choose the ele with max frequency as target and
# will make all ele to this target ele either by 'addition' or subtraction.

# so problem reduces to "find the max freq of any ele in arr" say = max_freq
# then our ans= n- max_freq.

# time= space= O(n)
