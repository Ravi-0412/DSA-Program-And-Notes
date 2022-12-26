# logic: '&' with '1' gives that bit , or 
# '&' with all '1' gives that number itself(or with all zero also give the number itself).

# so if we can somehow get '1' at kth position and '0' at other remaining position. 

# we can get '1' at kth position by left shifting '1' 'k-1' times then, 
# we can get 1 at kth position and '0' at other positions

# till here we will get the bit at kth position but there will be
# all zero beyond kth in right side so to get actual digit

# now right shift 'k-1' times , after that original bit will come at 
# last(LSB) and that will be our ans

def kth_bit(n,k):
    # left= 1<< k-1   # left shifting '1' ,'k-1' time
    # kth= n & left   # this will give the bit at kth position but till k-1 all be zero
    # right= kth >> k-1    # will give the final ans
    # return right

    return((n & (1<< k-1)) >> k-1)

    # other logic just do right shift 'k-1' times. After this kth bit will come at the rightmost position
    # so to get the kth bit just take 'And' with 1
    # return (n>> k-1) & 1
    
print(kth_bit(13,3))
print(kth_bit(14,3))
print(kth_bit(32,4))


# method 2: Right shift the number 'k-1' times then the kth bit wil come at rightmost side.
# Now return 0 if number is even else 1 OR simply return this curr number by taking '&' with '1'.

