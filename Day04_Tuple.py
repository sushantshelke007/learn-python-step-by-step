# tuple is immutable
#let's create the tuple

tup=(1,2,3,4,5,"mona","rock")  # we can store diff-diff datatypes in tuple like list
print(tup)
print(len(tup))                  # len() function used for find the lenth of tuple
print(tup[2:5])                   # slicing of the list

 
 
# imp: for storing one element in tuple we need to use ,
num=(1,)
print(num)     #if we don't write , then it's give "int" as a type not tuple



# Method's in tuple/in built fucntion's

   # i).index(value):return the first occurance 
num=(11,25,43,56,75,25,25)
print(num.index(75))  


    # ii).count(value):count total occurance
print(num.count(25))


