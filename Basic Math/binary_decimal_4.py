# 1: Converting decimal to binary
# print(bin(n).replace("0b",""))   # to convert decimal to binary
# e.g:
print(bin(10).replace("0b",""))

# by normal method:
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num%2, end="")
# OR
# def DecimalToBinary(num):
#     if num ==0:
#         return
#     DecimalToBinary(num // 2)
#     print(num%2, end="")

# 2: converting binary to decimal
# print(int('n',2))               # to convert binary to decimal , 
                                # '2' is any base from which you want to convert to decimal equivalent
# e.g:
print(int('1010',2))
print(int('1010',3))  # will convert '1010' in base 3 to decimal


# to calculate the hamming distance between two numbers
a=6
b=9
c=a^b
print(bin(c).replace("0b","").count('1'))   # will calculate the hamming distance bw two +ve integer