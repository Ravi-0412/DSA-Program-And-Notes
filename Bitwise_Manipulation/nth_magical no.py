# for finding the nth magical number , write 'n' in binary and add the sum of value of powers with base '5' taht will be the ans.
# e.g: if n==1(001) then ans= 0*5^3 + 0*5^2 + 1*5^1= 5, if n= 3(011) then ans= ans= 0*5^3 + 1*5^2 + 1*5^1= 30
# just like we convert binary to decimal but here base= '5' and powers count will start from rightmost side with '1,2,3....' .

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






