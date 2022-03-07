# hcf by euclid's algo
def hcf(a,b):
    if a==0:
        return b
    return hcf((b%a),a)

def lcm(a,b):
    return (int((a*b)/(hcf(a,b))))

print(hcf(6,32))
print(lcm(9,18))
