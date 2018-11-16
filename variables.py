# variables
#   Data types
#       Dynamic types
#           type: int, strings, floats, boolean

#   type variable = value
#   int age = 38 --> integer
#   reason for data types
#       allocation of space --> age would take up 2 spaces exceed 2 spaces error -- error handling -- amount of memory used
#       error handling --> exceptions age = five = or age = blue

# age = 23
# print (age)
# age = "twenty three" # reassignment of a variable
# print (age)


# nameOne = "Scott"
# nameTwo = nameOne

# print(" The first name " + nameOne + ' the second name ' + nameTwo)

# print(id(nameOne))
# print(id(nameTwo))
# nameOne = "John"

# print(" The first name " + nameOne + ' the second name ' + nameTwo)

# print(id(nameOne))
# print(id(nameTwo))

# nameTwo = "Bill"
# print("Bill 1")
# print(id(nameOne))
# print(id(nameTwo))

# nameTwo = "Bill"
# print("Bill 2")
# print(id(nameOne))
# print(id(nameTwo))

# Limited use on variables names
#yield = "yes"          ------> Reserved Words not allowed
#3dvariable = "cube"    ------> Starting with a number
# $testvariable = "$56" ------> Starting with symbol

# #variable notation
# the_underscore_variable = "recommended by python style guide"
# camelCaseVariable = "reccommended by Scott"
# NEVER_GOING_TO_CHANGE_VARAIBLE = "Scott"

#Numbers and variables
hexadecimalNumber = hex(34)
print(hexadecimalNumber)

binaryNumber = bin(34)
print(binaryNumber)

bigNumber = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(bigNumber)

# Strings

# String assigment and position
myFirstString = "Hello World"
print(myFirstString)
print(myFirstString[0])
print(len(myFirstString))


#string comparision
class1 = "CS 1030"
class2 = "CS 1030"
class3 = "CS 1400"

print(class1 == class2) # == you're checking the value, = means you're setting the value.
print(class2 == class3)

floatNumber = 3.09 
intNumber = 3

sumNumber = floatNumber + intNumber
print(sumNumber)

# Boolean Variable 

isLightOn = True 
isLightOff = False