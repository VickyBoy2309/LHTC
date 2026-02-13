# Hello World
print("Hello World")

#Name & Age For Welcome
name = "Vicky_Boy_23😉";
age = 20;
print(f"Welcome back Mr.{name}");
print(f"Your age is {age}");

#Variable = A container for a value (String, Interger, Float, Boolean)
#           A variable behaves as if it was the vaule it contains

#String : strings are denote with "" {eg : name = "Vigneshwaran"}
#Inside the string everything know as character
first_name = "Vigneshwaran D";
email = "0987vickyboy@gmail.com";
print(first_name);
print(f"Hello {first_name}");
print(f"Your E-Mail is {email}");

#Integer : integer are used to store number values {eg : age = 20}
age = 20;
quantity = 3
num_of_students = 30 
print(f"You are {age} years old");
print(f"You are buying {quantity} items");
print(f"Your class has {num_of_students}");

#Float : float is a number but contains decimal portion {eg : age =  10.5}
price = 10.99;
gpa = 7.68;
distance = 10.6;
print(f"The Price is ₹{price}");
print(f"Your gpa is :{gpa}");
print(f"You ran {distance}km today")

#Boolean : boolean consists of only True or False it's also related with Binary[0 1] {eg : isRain = True}
#These boolean values starts with a captial value
is_student = True;
for_sale = False;
is_online = True

#if else for is_student
print(f"Are you a Student ? : {is_student}");
if for_sale :
  print("That item is for Sale")
else :
  print("That item is NOT for sale")

#if else for is_online  
if is_online :
  print("Your are Online")
else :
  print("Your are Offline")

#Typecasting : Typecasting is the process of converting a variable from one datatype to another 
#              str(), int(), float(), bool()
name = "Vigneshwaran D";
my_age = 20;
gpa = 7.68;
is_student = True;
print(type(name));
print(type(my_age));
print(type(gpa));
print(type(is_student));

#Trunning the datatype into another
gpa = int(gpa);
print(gpa);

#Examples for Typecasting int() into str()
my_age = str(my_age)
my_age += "1"
print(type(my_age))
print(my_age);

#Examples of Typecasting str() into bool()
name = bool(name)
print(name)

# Input() : A Function that prompts the user to enter data
#          Returns the entered data as a string

name = input("What is your name ?: ")
age = int(input("How old are you ?:"))
age = age + 1
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"{age} years old")

#Exercise 1 Rectangle Area Calc
length = float(input("Enter the length :"))
width = float(input("Enter the Width :"))
area_of_rectangle = length * width
print(f"The area of the rectangle is {area_of_rectangle}cm²")

#Exercise 2 Shopping cart Program
item = input("What item do you want ? :")
price = float(input("What is the price ? :₹"))
quantity = int(input("How many of that you want ? :"))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Total = ₹{total}")