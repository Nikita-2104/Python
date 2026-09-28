age = int(input("Enter your age:"))
# Starting of the if statement : 2
if (age % 2 == 0):
    print("n is even.")
# End of the if statement : 1
# Starting of the if statement : 2
if (age >= 18):
    print("Your age is valid.")
elif (age < 0):
    print("You are entering wrong age.")
else:
    print("Good for you.")
# End of the if statement : 2
print("End of the program")


a = int(input("Enter the first no.:"))
b = int(input("Enter the second no.:"))
c = int(input("Enter the third no.:"))
d = int(input("Enter the fourth no.:"))
if ( a > b and a > c and a > d):
    print("A is the Greatest number.")
elif (b > a and b > c and b > d):
    print("B is the Greatest number.")
elif (c > a and c > b and c > d):
    print("C is the Greatest number.")
else:
    print("D is the Greatest number")


sub1 = int(input("Enter the marks:"))
sub2 = int(input("Enter the marks:"))
sub3 = int(input("Enter the marks:"))
total_average = (100*(sub1 + sub2 + sub3))/300
if(total_average >= 40):
    print("You are pass.")
else:
    print("You are fail!")



m1 = "only now"
m2 = "apply now"
m3 = "make a lot of money" 
m4 = "subsribe this"
msg = input("Enter your message:")
if ((m1 in msg) or (m2 in msg) or (m3 in msg) or (m4 in msg)):
    print("Spam Message!")
else:
    print("It's safe.")



username = input("Enter your username : ")
if (len(username) < 10):
    print("Your username is Valid..!")
else:
    print("Your username is Invalid..!")



l = ["nikki" , "vanshuu" , "nidhi"]
name = input("Enter your name: ")
if (name in l):
    print("Your name is present in the list.")
else:
    print("Your name is not present in the list.")



marks = int(input("Enter your marks:"))
if (marks <= 100 and marks > 90):
    grade = "Ex"
elif (marks < 90 and marks > 80):
    grade ="A"
elif (marks < 80 and marks > 70):
    grade ="B"
elif (marks < 70 and marks > 60):
    grade ="C"
elif (marks < 60 and marks > 50):
    grade ="D"
elif (marks < 50 and marks > 40):
    grade ="E"
elif (marks < 40 and marks > 30):
    grade ="F"
print(f"Your grade is : {grade}")



post = input("Enter the comment:")
if ("nikki" in post):
    print("Yes this post is talking about you!") 
else:
    print("No This post is not talking about you!")