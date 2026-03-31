# List is the inbuilt datatype in python
# list is the mutable

marks=[1,2,3,4,5,"arjun","danny"]   # we can store diff-diff datatypes in list
print(marks)
print(len(marks))                    # len() function used for find the lenth of list
print(marks[3:6])                    # slicing of the list



 # Method's in list/in built fucntion's

  #i).append():adding somethings at the end of the list
marks.append("john")
print(marks)


   # ii).insert():inset the value anywhere just need to put index number
marks.insert(2,100)
print(marks)


   # iii).sort():sorting elements increasing order [Note:for sorting list must contains same datatype)
num=[34,56,9,100,3,4,5,60]   
num.sort()
print(num)   


    # iv).reverse():reverse the entire list
num.reverse()
print(num)


