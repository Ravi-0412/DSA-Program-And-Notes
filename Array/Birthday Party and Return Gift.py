def findKid(N, T, D):
    # first find the anser for 0- based indexing in this type of cyclic question.
    # (D + T- 1) : last one will be this person only because it will start from 'Dth person' so subtracting '-1'.
    ans = ((D + T- 1) -1) % N   # Again subtracting '-1' for bring into '0 - based' indexing.
    # for converting into 1-based indexing add '1'.
    return ans + 1
