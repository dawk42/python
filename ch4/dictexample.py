#!/usr/bin/python3

#create dictionary object
fn = { "1":"def pt(a,b):return (a**2+b**2)** 0.5 ","two":"dos","three":"tres" }

print (eng2esp)


print (eng2esp["one"])
print (eng2esp['three'])

#add and remove items from dictionary
eng2esp.update({"four":"cuatro","five":"cinco"})

#remove item from dictionary
eng2esp.pop("two")
print(eng2esp)

#show all keys and values
print(eng2esp.keys())
print(eng2esp.values())
