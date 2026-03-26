# String is immutable (means we can't change anything after defining any string)

# 1] string replication / we can print any string multiple times
  
name="sushant shelke"
print(name*3)


# 2] String Length

print(len(name))       # in the length spaces are also counted


# 3] String concatenate 

name="sushant"
L_name="shelke"
print(name+L_name)


# 4] String indexing   

print(name[0])       # to print any index 


# 5] string slicing (used to print any specific string by giving starting_index and ending_index)

str="i'm currently learning python"
print(str[5:15])


# 6] case conversion  (upper case - lowercase // just use .lower() & .upper() )

print(name.lower())        
print(name.upper())


# 7] String stripping  (basically used to remove extra spaces) 

print("   hello my name is shiv  ")   # in this some extra spaces are there, to remove them we use stripping [.strip]
print("   hello my name is shiv  ".strip())


# 8] String replacing 

print("sushant shelke".replace('s','*'))


# 9] String count

print("sushant shelke".count('s'))