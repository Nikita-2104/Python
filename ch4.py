#fruits = ["Apple", "Banana", "Mango"]
numbers = [1, 2, 3]
# print(sum(numbers))
print(())

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
t = (23, 56, 67, 45)
t[2] = 78
print(t)


l = [34, 56, 78, 56]
print(f"The sum the list's number is {sum(l)}")


t = (2, 4, 0, 8, 0, 6, 7, 0, 0)
print(t.count(4))