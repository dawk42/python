#!/usr/bin/python3

def pt(a,b):
    return (a**2+b**2) ** 0.5
print(pt(3,4))


def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result


#lists
numbers = [1,2,3,4,5,6,7,8,9,10]
# show the list
print(numbers)
#show 1 item from list
print(numbers[4])
#slice a list
print(numbers[2:4])
#slice a list with stride
print(numbers[1:10:2])


# Add to the end of a list
numbers.append(11)
#change values in the list
numbers[2]=50
#insert to a location in a list
numbers.insert(5,42)
#your can delete locations in the list with pop
numbers.pop(3)
print(numbers)

#Create a dictionary object

som = {'do':'a deer a female deer',
       're':'ray, a drop of golden sun',
       'mi':'me, a name I call myself',
       'fa':'far, a long, long way to run',
       'so':'sew, a needle pulling thread',
       'la':'la, a note to follow so',
       'ti':'tea, a drink with jam and bread'}
print(som)

#view elements of the dictionary
print(som['do'])
print(som['fa'])
print(som.values())
print(som.keys())
#remove an element from the dict.
som.pop('so')

#add an element to the dictionary

som.update({'so':'sew, a needle pulling thread'})








