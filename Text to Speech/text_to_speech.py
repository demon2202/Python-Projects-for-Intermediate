from gtts import gTTS
import os

text="hello, guys welcome to my github page"
language = 'en'

obj=gTTS(text = text, lang = language , slow = False)
obj.save("sample.mp3")
os.system("sample.mp3")


