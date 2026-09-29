# CHAPTER 1 NORMAL PYTHON PROGRAMS

# To print the poem
print("""
Twinkle, twinkle, little star,  
How I wonder what you are!  
Up above the world so high,  
Like a diamond in the sky."""
)


# It an voice module TEXT TO SPEECH
import pyttsx3
engine = pyttsx3.init()
engine.say("hey i am nikki")
engine.runAndWait()


# To find the contents of a directory
import os
directory_path = "Chapter4"
contents = os.listdir(directory_path)
print(contents)


# To print the contents of the directory
for item in contents:
     print(item)