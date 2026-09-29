# Chapter 2 - Python Data Types


# To print the data types of different variables
dict = {
    "Name" : "Nikita",
    "Age" : 20,
    "Course" : "B.E"
}
print("Name :", dict["Name"])
print("Age :", dict["Age"])
print("Course :", dict["Course"])



# to print data type of variable
a = "10"
t = type(a)
# print(t)
# b = 22
# print (a+b)
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
sum = a + b
print(sum)



# To print the remainder of two numbers
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
Remainder = a / b
print(Remainder)


# to print type of the character the user enter
a = int(input("Enter the 1st number:"))
print(type(a))


# to print the greatest number of two
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
print(a>b)



# to print an average of two numbers
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
print(f"Average of {a} and {b} is {(a+b)/2}")



# to print an square of an number
a = int(input("Enter the 1st number:"))
print(f"An Square of the number is {a*a}")