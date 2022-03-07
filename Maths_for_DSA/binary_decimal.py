print(bin(n).replace("0b",""))   # to convert decimal to binary
print(int('n',2))               # to convert binary to decimal


# e.g:
a=6
b=9
c=a^b
print(bin(c).replace("0b","").count('1'))   # will calculate the hamming distance bw two +ve integer