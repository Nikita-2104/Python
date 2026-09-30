# For loop with List
l = [1, 2, 3, "nikki"]
for i in l:
    print(i)
# For loop with Tuple
t = (2, 56, "good", 214) 
for i in t:
    print(i)
# For loop with String
s = "Nik"
for i in s:
    print(i)


# to print myname 5 times
i = 0
while (i < 5):
    print("Nik")
    i += 1 


# FOR LOOP WITH STRINGS
name = "NIKKI"
for latter in name:
    print(latter)


# FOR LOOP WITH LISTS
list = ["nik", "piyu", "nidh"]
for name in list:
    print(name)


# FOR LOOP WITH TUPLE
tuple = (1, 3, 23, "me")
for numbers in tuple:
    print(numbers)


# FOR LOOP WITH DICTIONARY
dict = {
    "name" : "nik",
    "age" : 20,
    "city" : "ankleshwar"
}
for details in dict.items():
    print(details)



# FOR LOOP WITH SET


clr = {"Red", "pink", "blue"}
for color in clr:
    print(color)



# WHILE LOOP WITH LIST

i = 0
while i <= 5:
    print(i)
    i += 1


# PRINTING STARS
# Code for printing stars pattern

n = int(input("Enter the number:"))

for i in range(1, 6):
    print("*" * i)
    i += 1

# Code  printing numbers
for i in range(3):
    for j in range(2):
        print(i, j)


for i in range(1, 10+1):
    print(i)
    i += 1


for i in range(10, 0, -1):
    print(i)
    # i -= 1

for i in range(2, 21, 2):
        print(i)
        i += 1


for i in range(1, 21, 2):
        print(i)
        i += 1

n = int(input("Enter the number:"))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
    i += 1


i = 1
while i <= 10:
    print(i)
    i += 1



total = 0
for i in range(1, 101):
    total += i
print(total)

n = int(input("Enter the number:"))
for i in range(n):
    if n == 0 and n == 1:
        print(1)
    fact = n * n-1
print(fact)

n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


n = int(input("Enter number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)


n = int(input("Enter number:"))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)

n = int(input("Enter the number:"))
for i in range(n):
    print("*" * n)
    i += 1

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()


n = int(input("Enter number:"))
for i in range(n):
    print("*" * i)


n = int(input("Enter number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*",end="")
    print()



for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


 

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


n = int(input("Enter number:"))
count = 0
for i in range(1, n + 1 ):
    if n % i == 0:
        count += 1 
if count == 2:
    print("Yes this is prime number.")
else:
    print("This is not prime number.")



for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)


a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b


numbers = [12, 45, 67, 395, 23, 78, 90]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)


text = input("Enter text: ")

count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print(count)


for i in range(50, 101):
    print(i)



for i in range(7, 101, 7):
    print(i) 



num = 0
for i in range(2, 101, 2):
    num += i
print(f"Sum = {num}")
 


for i in range(1, 21):
    if i % 3 == 0:
        print(i)


total = 0
for i in range(1, 11):
    total = total + i
print(total)


for i in range(5, 0, -1):
    print("*" * i)


for i in range(1, 6):
    print(str(i) *i)


for i in range(3):
    for j in range(1, 4):
        print(j, end="")
    print()




for i in range(3):
    for j in range(1, 4):
        print("*" * j, end="")
    print()




for i in range (1, 6):
    for j in range(i):
        print("*", end="")
    print()


for i in range (5, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()

even = 0
odd = 0  

for i in range(1, 21):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even = {even}")
print(f"Odd = {odd}")




for i in range():


numbers = [4, 2, 7, 1]
print(numbers)
print(f"Max {max(numbers)}")
print(f"Min {min(numbers)}")
print(f"Sum {sum(numbers)}")
print(f"Len {len(numbers)}")




