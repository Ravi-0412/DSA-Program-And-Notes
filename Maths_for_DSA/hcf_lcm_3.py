# hcf by euclid's algo
# time: O(log(min(a, b))
# just same as we calculate the hcf on paper 
def hcf(a,b):
    if a==0:
        return b
    return hcf((b%a),a)  # or hcf(a,(a%b))

# other method ,diff is working same as '%'
# same logic as above, here we are taking difference instead of '%'
# so checking which one is greater first
def hcf(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return hcf((a-b),b)
    return hcf(a,b-a)
# or use the same above logic with DP


def lcm(a,b):
    return (int((a*b)/(hcf(a,b))))  # By 'Lcm*Hcf= Product of two number'

print(hcf(6,32))
print(lcm(9,18))
