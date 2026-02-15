# Day - 2 : 15/02/2026 - Bro Code Python Full Course 32:40 - 51:45
# Madlibs Game
# Word game where you create a story
# By filling in blanks with random words

#Bro Code's Code
adjective1 = input("Enter an adjective (Description):")
noun1 = input("Enter a noun (Person, Place, Thing):")
adjective2 = input("Enter an adjective (Description):")
verb1 = input("Enter a verb endig with 'ing'")
adjective3 = input("Enter an abjective (Description):")
print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

#My example 
adjective4 = input("Enter a Adjective :")
noun = input("Enter a noun :")
verb2 = input("Enter a verb :")
place = input("Enter a place :")
animal = input("Enter a animal :")
emotion = input("Enter a emotion :")
food = input("Enter a food :")
verb3 = input("Enter a verb :")
celebrity_name = input("Enter a celebrity name :")
number = input("Enter a number :")
adjective5 = input("Enter a adjective :")
print(f"Yesterday, I saw a {adjective4} {noun} that suddenly {verb2} all the way to {place}.")
print(f"Everyone was shocked when a {animal} appeared and started shouting with {emotion}!")
print(f"Out of nowhere, someone threw a giant {food} while people were {verb3} in confusion.")
print(f"Then, {celebrity_name} showed up and said, “This is the most unbelievable thing I’ve seen in {number} years!”")
print(f"In the end, we all agreed it was the most {adjective5} day of our lives.")

#Arithmetic operators (Math Functions)
friends = -5 #Base Variable

#Augmented Operator (Assignment)
friends += 1 #Addition
friends -= 2 #Subtraction
friends *= 3 #Multiplication
friends /= 2 #Division
friends **= 2 #Exponentiation
friends %= 2 #Modulus

# Arithmetic Operator (Mathematical)
friends = friends + 1 #Addition
friends = friends - 1 #Subtraction
friends = friends * 3 #Multiplication
friends = friends / 3 #Division
friends = friends ** 2 #Exponentiation
friends = friends % 2 #Modulus

print(int(friends)) #Print with math execution

#Variables
x = 3.14
y = -4
z = 5

result = round(x) #Round the number to it's nearest value
result = abs(y) #abs() used to print absolute number , which is the distance away from zero as a whole number
result = pow(z , 3) #pow() used to Exponentiation with parameter such as {eg : (base , power)}
result = pow(z , 3 , 3) #pow() with modulus , which is used to calculates the modulus of the Exponentiation and return as a final output
result = max(x, y, z) #max() used to return the maximum value among the variables
result = min(x, y, z) #min() used to return the minimum value among the variables

print(result)

# import the math module
import math #Math Module

x = 9.9 #Variable

result = math.sqrt(x) #math.sqrt() used to find square root of the value or variable
result = math.ceil(x) #math.ceil() used to round up the number , which is round upward
result = math.floor(x) #math.floor() used to round down the number which is round downward

print(math.pi) #math.pi used to work with pi(π) value 
print(math.e) #math.e used to work with Euler's number(e) value
print(result)

#Exercise 1 Circumference of a circle
import math

radius = float(input("Enter the radius of a circle :"))
circumference = 2 * math.pi * radius

print(f"The circumference is : {round(circumference , 2)}cm")

#Exercise 2 Area of a circle
import math

radius = float(input("Enter the radius of a circle :"))

area = math.pi * pow(radius , 2)

print(f"Area of the circle is : {round(area , 2)}cm²")

#Exercise 3 Hypotenuse of a right triangle
import math

a = float(input("Enter Side A :"))
b = float(input("Enter Side B :"))
c = math.sqrt(pow(a , 2) + pow(b , 2))

print(f"Side C = {c}")