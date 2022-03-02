class computer:

    def __init__(self,cpu,ram):
 #used to initialise the variable for every object. just same as constructor in c++ and java   
 #The 'self' in Python is equivalent to the this pointer in C++ and the this reference in Java and C#
 # Self is always pointing to Current Object.
 # Self is always required as the first argument
        self.cpu=cpu
        self.ram=ram        
          
    def config(self):  # method for printing data members
        print("config is:",self.cpu,self.ram)
#since cpu and ram itself is an object so writing only cpu and ram will not work
        
comp1= computer('i7', 16)
comp2= computer('i5', 8)
# print(type(com1))
# computer.config(comp1)
# computer.config(comp2)
comp1.config()
comp2.config()

