from abc import ABC, abstractclassmethod

class computer(ABC):   #class containing abstract methods are 'abstract class'
    @abstractclassmethod
    def process(self):   # methods which have only declaration,no definitions are 'abstract method'
        pass

class laptop(computer): #class inhereting a abstract class also become abstract class if you don't define any method inside it
    def process(self):
        print("its running")

# c1= computer()   # will result into error, object of abstract class can't be created
com1=laptop()
com1.process()



'''
Difference between abstract class and duck typing

This is an exam 'hall' and there are students from 2 diffrent 'classes' seated. Class A has a maths test, Class B has social.

The invigilator says that to enter the hall, every one must carry an instrument box. Now students of classes both A and B must bring one even if B class don't have its use. So the class A will have a set of compass, rulers, pencils etc in it. But since students of class B don't have any use, they will just bring one with a pencil or even just empty (pass) because its compulsory to bring one in to be in the hall.

If a parent class has an abstract method, every child must also have one. So each child will have to define one of thier own.

In duck typing, It isn't necessary to define the parent class method for each child classes. it just simply have to point to the class where the particular method lies. Here we would have to define for each.

'''