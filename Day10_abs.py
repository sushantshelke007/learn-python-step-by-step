# Abstraction:  hiding internal details and showing only the important features to the user.
 # for implement abstraction in python we use the abstract class
    # abstarct class is the part of abc module(module means already code written by any programmer)

# in abstraction class we not implement the anything we perfrom the another class



from abc import ABC,abstractmethod          #here ABC is abstraction based class,

class human():
    @abstractmethod          # because of this python knows this is abstarct clas
    def work(self):
        pass                # here we created the abstract class,we write the pass which reperesnt the null value

class male(human):
    def work(self):
        print("i can work")

m1=male()
m1.work()        

