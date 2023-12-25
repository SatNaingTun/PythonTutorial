import pyttsx3
import os

mytext="This is BOC. Best Oil 4 Best Car"
voice=pyttsx3.init()
voice.say(mytext)
voice.save_to_file(mytext,"hello.mp3")
voice.runAndWait()
