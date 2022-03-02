# stock prices on a given date
# 1st using list


# ?? don't know why this program not working

# stock_prices= []
# with open("stock_prices.txt","r") as f:
#     for line in f:
#         tokens= line.split(',')
#         day= tokens[0]
#         price= float(tokens[1])
#         stock_prices.append([day,price])
# print(stock_prices)


# example implementing dictionary using hash map

class HashTable:
    def __init__(self):
        self.MAX= 10  #assuming max no in array =100
        self.arr= [None for i in range(self.MAX)]    # INITIALISING all elements with 'None'

    def get_hash(self,key):
        h=0
        for char in key:
            h+= ord(char)  #will sum up the ascii value all the characters of key
        return h%self.MAX  
    # now for adding key value pair
    def __setitem__(self,key,val):
        h= self.get_hash(key)
        self.arr[h]= val
    #for getting value by calling a key
    def __getitem__(self,key):
        h= self.get_hash(key)
        return self.arr[h]
    # deleting value at a particular key
    def __delitem__(self,key):
        h= self.get_hash(key)
        self.arr[h]= None

t= HashTable()
print(t.get_hash('march 6'))   #will give '9
# t.add('march 6',130)           # 130 will get inserted at index 9 in the array
# print(t.arr)
# print(t.get('march 6'))
t['march 6']= 130         # will call setitem and will set the value 130 according to corresponding key
t['march 1']= 20
t['dec 17']=  30
print(t.arr)
print(t['march 6'])       # will return the value at key 'march 6'
t.__delitem__('march 6')
print(t.arr)





