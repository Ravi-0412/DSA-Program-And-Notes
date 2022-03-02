class computer:
    def __init__(self):
        self.name="ravi"
        self.age=28
    
    def compare(self,other):
        if self.age== other.age:
            return True
        else:
            return False
        

c1= computer()
c1.age= 30
c2= computer()
 
c1.name= 'raushan'
# # print(id(c1))  #gives the address of c1
print(c1.name)  # since for c1 we are explicitly giving the name
                # the given name will be get assigned to c1
print(c2.name)  # since for c2 we are not explicitly giving the name
                # the name in constructor  will be get assigned to c2

if c1.compare(c2): #since c1 calling so c1 will be self and other will be c2
    print("they are same")
else:
    print("they are different")
