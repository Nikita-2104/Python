student = {
    "name": "Nikita",
    "age": 20,
    "city": "Vadodara"
}

print(max(student))

words = {
    "chalvu" : "walking",
    "madad" : "help",
    "haa" : "yess",
    "naa" : "noo"
    
}  
word = input("Enter the word:")
print(words[word])


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


s = {}
print(type(s))


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


s = {8, 7, 12, "nikki", [1,2]}
# s.add()
s[4][0] = 9
# we cant change the value stored in the list in set


s = set()#empty set is created
print(type(s))

