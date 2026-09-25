print("""
Twinkle, twinkle, little star,  
How I wonder what you are!  
Up above the world so high,  
Like a diamond in the sky."""
)

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hey i am nikki")
engine.runAndWait()

import os

directory_path = "Chapter4"
contents = os.listdir(directory_path)

print(contents)
# for item in contents:
#     print(item)