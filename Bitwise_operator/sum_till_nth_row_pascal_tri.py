# Q: find sum of all ele till nth row in pascals triangle
# sum= 2^n -1
def sum(n):
    sum=0
    for i in range(n):
        sum+= 1<<i
    return sum
print(sum(5))


# Q: find sum of all ele of the  nth row in pascals triangle
# sum= 2^(n-1)
def sum(n):
    return 1 << n-1
print(sum(5))

# note: when you have to do operation in pow of two
# alwalys think of left shifting '1'

