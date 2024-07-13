def findKid(N, T, D):
    # first find the anser for 0- based indexing in this type of cyclic question.
    ans = (D - 1 + T- 1) % N
    # for converting into 1-based indexing add '1'.
    return ans + 1