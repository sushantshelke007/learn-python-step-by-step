# inheritance: basically mena sthe inherite property from parent class

 # parent class -- child class



  #i) single level inheri: (parent pro inheri by child class)

class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class male(human):
    def sleep(self):
        print("i can sleep")
        print("--------------------")

m1=male()
m1.eat()
m1.work()
m1.sleep()                    


   # ii) multilevel inheri:(A--B--C)
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
 
class male(human):                     # male inherit prop from human
    def sleep(self):
        print("i can sleep")

class boy(male):                       # inheri prop from male means indirectly from the human       
    def gym(self):
        print("i can gym")
        print("------------")

b1=boy()
b1.eat()
b1.work()
b1.sleep()
b1.gym()                   


    # Hierarchical Inheritance: one parent ,many child
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class male(human):
    def sleep(self):
        print("i can sleep")
class female(human):
    def cook(self):
        print("i can cook")
m1=male()
m1.sleep()
m1.eat()
m1.work() 
f1=female()
f1.cook()
f1.eat()
f1.work()  
                       

