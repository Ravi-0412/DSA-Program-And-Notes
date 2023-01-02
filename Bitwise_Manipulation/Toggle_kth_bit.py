# for toggling use the concept of xor at that position with '1'
# since xor of any number with '1' is the negation of that number and
# xor of any no with 'zero' is that number itself

# so  first bring '1' at that position keeping all the position '0'

def Toggle_kth(n,k):
    return n^(1<< k-1) 
