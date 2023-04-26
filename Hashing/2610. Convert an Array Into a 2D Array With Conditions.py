# row should not contain duplicate and we need only miniml number of rows.

# logic: This means no of row must be= max(freq) of any ele to have all distinct ele in each row.
# And for filling up each row traverse each distinct ele(key in dictionary) and check if its freq >=1 (still some ele remaining to include) 
# then include the cur ele in row(curAns)

# time: no_row * no_distinct_ele.

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq= Counter(nums)
        row_no= max(freq.values())    # shortcut to get val in dictionary
        
        ans= []
        for i in range(row_no):
            curAns= []
            for key, val in freq.items():
                if val >= 1:
                    curAns.append(key)
                    # val-= 1  # won't change the value
                    freq[key]-= 1
            ans.append(curAns)
        return ans
    

# no need of numset, w