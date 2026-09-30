# simple code to print fruits nd sum of num
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
numbers = [1, 2, 3]
print(sum(numbers))
print(())



# to print the furits name user wants to insert in list
fruits = []
f1 = input("Enter the fruit name:")
fruits.append(f1)
f2 = input("Enter the fruit name:")
fruits.append(f2)
f3 = input("Enter the fruit name:")
fruits.append(f3)
f4 = input("Enter the fruit name:")
fruits.append(f4)
f5 = input("Enter the fruit name:")
fruits.append(f5)
f6 = input("Enter the fruit name:")
fruits.append(f6)
f7 = input("Enter the fruit name:")
fruits.append(f7)
print(fruits)




# to print the marks user wants to insert in list
marks = []
m1 = input("Enter the marks:")
marks.append(m1)
m2 = input("Enter the marks:")
marks.append(m2)
m3 = input("Enter the marks:")
marks.append(m3)
m4 = input("Enter the marks:")
marks.append(m4)
m5 = input("Enter the marks:")
marks.append(m5)
m6 = input("Enter the marks:")
marks.append(m6)
m7 = input("Enter the marks:")
marks.append(m7)
marks.sort()
print(marks)



# We cant change or modify the tuple becuse it is IMMUTABLE 
# So this code will gives an error
t = (23, 56, 67, 45)
t[2] = 78
print(t)



# to print the sum of numbers stored in list
l = [34, 56, 78, 56]
print(f"The sum the list's number is {sum(l)}")



# count fun will count that how many times 4 is appears in ur list
t = (2, 4, 0, 8, 0, 6, 7, 0, 0)
print(t.count(4))