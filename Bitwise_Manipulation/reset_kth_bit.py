# index start from '1' from LSB
# for reset we use 'AND' with '0'. 
# to get '0' keeping other bit same with '&'. we must get '0' at kth position and 
# all other position it must be '1' since we are doing '&' we want bit at remaining position as it is.

# shift '1' by 'k-1' and negate it(1's complement: 0->1, 1->0)
# after that take 'AND' of this with the number given

# for toggling use the concept of xor at that position with '1'
# since xor of any number with '1' is the negation of that number

def reset_kth(n,k):
    return (~(1<< k-1) & n)
    
print(reset_kth(5,1))
print(reset_kth(5,2))


