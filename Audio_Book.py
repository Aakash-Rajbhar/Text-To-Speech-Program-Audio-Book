#Import gtts and from gtts import gTTS(Google Text To Speech) module.
from gtts import gTTS 

#Import os module
import os

mytext='''Hello Aakash'''      #The text you want to covert into speech

language='en'                   #Selecting the language
myobj = gTTS(text=mytext,lang=language, slow=False)
myobj.save("audio.mp3")
os.system("audio.mp3")
