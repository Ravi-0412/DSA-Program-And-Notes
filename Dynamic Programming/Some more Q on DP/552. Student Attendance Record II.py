# understand using solution in link and chatgpt

# time = space = O(6* n) 

class Solution:
    def checkRecord(self, n: int) -> int:
        # Define the modulo value
        MOD = 1000000007
        
        # Initialize a 3D array to store the counts of valid attendance records
        # f[i][j][k] denotes the count of valid sequences of length i where:
        # - There can be at most j A's in the entire sequence.
        # - There can be at most k trailing L's.
        f = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Base case: one record of length 0, with all possibilities for 'A' and 'L'
        f[0] = [[1, 1, 1], [1, 1, 1]]

        # Dynamic programming loop to fill the array for all record lengths
        for i in range(1, n + 1):
            for j in range(2):  # 'A' count
                for k in range(3):  # Consecutive 'L' count
                    # Initialize the value with the count from the previous day's record
                    val = f[i - 1][j][2]  # Previous day ended with 'P'
                    
                    # If there are 'A's left to use, add the count from the previous day with one less 'A'
                    if j > 0:
                        val = (val + f[i - 1][j - 1][2]) % MOD  # Previous day ended with 'A'
                    
                    # If there are 'L's left to use, add the count from the previous day with one less consecutive 'L'
                    if k > 0:
                        val = (val + f[i - 1][j][k - 1]) % MOD  # Previous day ended with 'L'
                    
                    # Store the calculated count for the current day's record
                    f[i][j][k] = val

        # Return the count of valid records for length n, ending with one 'A' and at most two consecutive 'L's
        return f[n][1][2]
    