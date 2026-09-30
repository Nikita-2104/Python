# to print the max value of the dictionary we can use max() function
student = {
    "name": "Nikita",
    "age": 20,
    "city": "Vadodara"
}
print(max(student))



# to print an eng meanig of this words
words = {
    "chalvu" : "walking",
    "madad" : "help",
    "haa" : "yess",
    "naa" : "noo"
    
}  
word = input("Enter the word:")
print(words[word])




# to print an empty set you hae to use set() function 
# bcz {} is used to create an empty dictionary
s = set()
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
n =input("Enter the no.:")
s.add(int(n))
print(s) 



# to pirnt an differ datatypes bt it defines that 
# even an int is in "" it will be count as string 
s = set()
s.add(18)
s.add("18")
print(s)
s = set()
s.add(20)
s.add("20")
s.add(20.0)
print(s)
# So the questoin is What is the length of the set?
# the ans is 2 bcz 20 = 20.0



#  so the type of this s is dict bcz an empty set is defined as set()
s = {}
print(type(s))



# to print the name and fav language of the user in dictionary
dict = {}
name = input("Enter the name:")
lang = input("Enter your fav language:")
dict.update({name : lang})
name = input("Enter the name:")
lang = input("Enter your fav language:")
dict.update({name : lang})
name = input("Enter the name:")
lang = input("Enter your fav language:")
dict.update({name : lang})
name = input("Enter the name:")
lang = input("Enter your fav language:")
dict.update({name : lang})
print(dict)




# to change the value stored in list in the dict
s = {8, 7, 12, "nikki", [1,2]}
# s.add()
s[4][0] = 9
# we cant change the value stored in the list in set



# to create an empty set
s = set()
print(type(s))

