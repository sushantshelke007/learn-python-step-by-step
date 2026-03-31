# Dict is the mutable
#Dict used when we have mutliple variables(keys) & we need to combine lot's of dta
#key:value pairs

dict={
    "F_name" : "central",
     "L_name" : "cee",
     "prof" : "rapper",
     "country" : "USA",
     "age" : 25

}
print(type(dict))
print(dict)
print(dict["country"])


# inbuilt function in dict

  # i).keys();return all the keys
print(dict.keys())


  # ii) .values():return the all values
print(dict.values())

   # iii) .items : return the key value pairs
print(dict.items())


  # iv) .update() : adding the item in the dict
dict.update({"song":"B4B"})
print(dict)


  # Nested dict:
dictt={
    "F_name" : "central",
     "L_name" : "cee",
     "prof" : "rapper",
     "country" : "USA",
     "age" : 25,
     "songg":{           # here we create the nested dict
         "i":"b4b",
         "ii":"life",
         "iii":"sad"
     }

}
print(dictt["songg"]["i"])


