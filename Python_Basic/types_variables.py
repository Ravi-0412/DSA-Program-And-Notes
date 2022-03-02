class car:
    wheels= 4    
    def __init__(self):
        self.mil= 10
        self.com= 'BMW'

c1 =car()
c2= car()
c1.mil = 8     #will affect only c1 since mil is a object variable
car.wheels =5  #will affect  all the objects since wheels is a class variable
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)