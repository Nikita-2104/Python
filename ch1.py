print("""
Twinkle, twinkle, little star,  
How I wonder what you are!  
Up above the world so high,  
Like a diamond in the sky."""
)

import pyttsx3
engine = pyttsx3.init()
engine.say("hey i am nikki")
engine.runAndWait()


import os
directory_path = "Chapter4"
contents = os.listdir(directory_path)
print(contents)
# for item in contents:
#     print(item)