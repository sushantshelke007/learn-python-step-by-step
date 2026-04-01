class student:                            # Creating class as student
    clg_name="sveri"                      # clg_name & stu_name is the class attribute
    stu_name="simon"


s1=student()            # here we created the object s1 we can crate more like s2,s3,.....,sn
  #print(s1.clg_name)      # using the "." operator we print the attribute which we want
  #print(s1.stu_name)


# constructor: -__init__
class bank():
    def __init__(self,cus_name):             #slef is the bydefault para in __intit__ method
        self.cus_name=cus_name

cus1=bank("rahul")
cus2=bank("rony")      
  #print(cus1.cus_name)
 #print(cus2.cus_name)



# types of construcotr/__init__ method:

  # i) default:only one para (self) 
  # ii)parameterized: in that more para is there eg:   def __init__(self,name,age,......)



# 4 Pillors of the oops

 # i) Encapsulation: contain the data and methods(function) in the sg unit like above code
  
    #whatever the attributes we provide above basically they are public means anyone can access

     # it is also used for the data protection,privacy
      # for private we use ( __ ) and protected ( _ )

class bank():
    def __init__(self,name,password):
        self.name=name
        self.password=password

cus1=bank("john",9552)
print(cus1.name,cus1.password)     

 # here it give error for the password because we make the attribute is protected
 # for access protected( __ ) attributes we use the getter,setter   

   # GETTER & SETTER: Basically it is like function,we can write in the class     

class bank():
    def __init__(self,name,password):
        self.name=name
        self.__password=password

    def get_password(self):
        return self.__password    

cus1=bank("john",9552)
print(cus1.name, cus1.get_password())  

