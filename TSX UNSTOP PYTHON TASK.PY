# Write a simple Python script that prints your name and a greeting. 
print("Hello, a very warm greetings !")
print("MY NAME IS ANUSHKA RATHOUR")


#  Write a script with comments explaining different parts of the code.
name = "Anu"  # Store your name in a variable
print("Hello, " + name + "!")  # Print greeting with name


# Write a script to calculate the area and perimeter of a rectangle using variables. 
# Dimensions
length = 5
width = 3

# Calculations
area = length * width
perimeter = 2 * (length + width)

# Output
print("Area:", area)
print("Perimeter:", perimeter)


#Write a script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number .
# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Comparison
if a > b:
    print("First number is greater.")
elif a < b:
    print("First number is smaller.")
else:
    print("Both numbers are equal.")


# Write a script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400). 
year = int(input("Enter a year: "))

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


#Write a script that concatenates two strings and prints the result.
first = "Global"
second = "Warming"
combined = first + " " + second
print(combined)
