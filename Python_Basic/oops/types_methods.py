import stat


class student:

    school= "RPS"

    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    
    @staticmethod   #fro function neither realted to class or instance you have to write this before that function
    def info():  
        print("This is a student class....")

    @classmethod    #before function related to class variable you have to write this before that function
    def getschool(cls):  #for working with class variable use 'cls' and for instance variable use 'self'
        return cls.school


s1= student(50,80,70)
s2= student(90,85,75)
print(s1.average())
print(s1.get_m1())
print(s1.getschool())      #print(student.info()) 
print(student.info())

