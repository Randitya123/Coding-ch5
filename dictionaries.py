dict={"Name":"Randitya","Age":14,"Gender":"Male","Gender":"F"}
print(dict)
   
#len of dictionary
print(len(dict))
#adding a new value
dict["new"]="yes"
print(dict)
dict["Name"]="yes"
print(dict)
#removing a new value
del dict["Name"]
print(dict)

dict.pop("Age")
print(dict)

#some extra methods
print(dict.keys())
print(dict.values())
print(dict.items())
