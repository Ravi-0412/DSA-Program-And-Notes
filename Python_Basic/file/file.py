# f= open("ravi.txt",'w')
# f.write("ravi is a good boy \n")
# f.write("he has a very good and helping nature")
# f.close()

f= open("ravi.txt",'r')
# print(f.read(4))
# print(f.read(10))
# print(f.tell())
f.seek(0)
for line in f:
    print(line)