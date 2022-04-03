# index start from '1' from LSB
# for reset we use 'AND' with '0'
# to get '0' keeping other bit same
# so left side 'k-1' times , and negate this
# after that take 'AND' of this with the number given

def reset_kth(n,k):
    return (~(1<< k-1) & n)
    
print(reset_kth(5,1))
print(reset_kth(5,2))
