# Logic: Similar to fibonacci
# Explanation: for n = i
# frequency of number from '1' to 'i' = sum of freq of all numbers of 'i-1' + 'i-2'.
# except for 'i' and 'i-1'.
# for 'i' , it will be equal to '1' and for 'i-1' it will come from 'i-1'.

# For base case we need to initialise for n = 1 and n = 2. (same way we initialise 2 values in fibonacci).

def count_children(n):
    freq = [{} for i in range(n + 1)]  # each index 'i' will store a dictionary which tells the frequency
                    # of number from '1' to 'i' i.e it wil give ans for n = i
                    # i.e freq[5][3] = will give frequency of '3' when n = 5
    # Initialise the base case
    freq[1][1] =  1 
    freq[2][1] =  1 
    freq[2][2] =  1
    # Now find ans for remaining
    for i in range(3, n + 1):
        freq[i][i] =  1   # freq of 'i' when n = i , will be '1' only
        freq[i][i - 1] = freq[i -1][i -1]   # freq of 'i -1' when n = i, will come from 'i-1'
        # except 'i' and 'i-1' , add the frequency of all other
        for j in range(1, i -1):
            # freq of 'j' when n = i => sum of freq of 'j' when n = i -1 &  n = i - 2
            freq[i][j] = freq[i- 1][j] + freq[i -2][j]

    ans = [0]*(n + 1)
    for key, val in freq[n].items():
        ans[key] = val
    return ans[1: ]
    
# n = 5
# n = 4
n = 6
print(count_children(n))

# Alternative and best solution:
# ans  = fibonacii pattern of 'n' in reverser order.
# e.g: n = 4 =>  3,2,1,1
# n = 5 => 5,3,2,1,1
# n = 6 => 8, 5, 3, 2, 1, 1