# Q: powers of 5(short)

def nth_magical(n):
    # multiply the rightmost bit till number becomes '0' by power of 
    # '5' by incr power by '1' in each iteration

    # for getting the  rightmost bit in each iteration 
    # '&'with '1'

    i=1
    num=0
    while(n>0):
        right_most= n & 1
        num+= right_most*pow(5,i)
        i+= 1
        n= n>>1  # do right shift one to get next right most bit
    return num

print(nth_magical(5))
print(nth_magical(6))






