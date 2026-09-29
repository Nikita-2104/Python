# Chapter 3 Escape Sequence Charater  
# \n used for giving new line
a = "hey i am nikita \n and i am a student"
print(a)



# \t used for tab giving space
a = "hey i am nikita \t and i am a student"
print(a)



# \" \" use for giving commas to a single world
a = "hey i am nikita \"nik\" and i am a student"
print(a)



# ALL OPERATIONS OF STRINGS

# Create a simple string
s = "hello i am nikki"

# access charater
print(f"Access the characters in string : \n {s[1]}")

# Negative Indexing
print(f"Negative Indexing : \n {s[-1]} ")

# Slicing
print(f"Slicing : \n {s[1:2]} ")

# Conantenation mix two string
print(f"Conatenation : \n {"nikki" + "solanki"}")

# Repetations
print(f"Repetation : \n {"hello" * 3}")

# Length of the string
print(f"Length of string : \n {len(s)}")

# Membersship
print(f"Membership : \n {"H" in s}")

# Comparison of string
print(f"Comparison of string : \n {"nik" == "nik"}")
print(s)



# to print good morning with user input name
name = input("Enter a name:")
print(f"Good Morning {name}")


# to write letter
letter = """
           Dear name
           You are selected!
           date
           ...
         """
print(letter.replace("name","Nikita").replace("date","4 Octomber 2026"))



# to fing double spaces 
name = "Hey  i am nikki i am a good  girl"
print(name.find("  "))



# letter writting in short way
Letter = "Dear Nikita,\n This is python course is nice.\nThanks! "
print(Letter)



# String Operations
name ="nikki"
print(name[-3:-1])
print(name[1:3])


# Strings Operations
print(len(name))
print(name.upper())
print(name.capitalize())
print(name.startswith("ki"))
print(name.endswith("ki"))
print(name.count("k"))
print(name.replace("n","v"))
print(name.find("n"))
print(name.split(","))
print(name.strip())

