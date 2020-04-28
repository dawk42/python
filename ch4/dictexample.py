#!/usr/bin/python3

#create dictionary object
eng2esp = { "one":"uno","two":"dos","three":"tres" }

print (eng2esp)


print (eng2esp["one"])
print (eng2esp['three'])

#add and remove items from dictionary
eng2esp.update({"four":"cuatro","five":"cinco"})

#remove item from dictionary
eng2esp.pop("two")
print(eng2esp)
