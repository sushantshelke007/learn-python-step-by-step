# set is the mutable
sett={1,2,3,3,3,}      # sets take the repate values just once's 
print(sett)             
print(len(sett))   

# Method's in set/in built fucntion's

 # i) add(): add the value in set
sett.add(100)
print(sett)


# ii) remove(): remove the value in set
sett.remove(100)
print(sett)


# iii) clear(): empty the set
sett.clear()
print(sett)


# iv) pop(): remove the random value from set
sett.clear()
print(sett)


 # Now to important functions i)union() ii)intersection 

   # i) union(): it print the all values in both sets
s1={1,2,3,4}
s2={7,8,9,4}
print(s1.union(s2))


   # ii) intersection():it print the comman values
print(s1.intersection(s2))
