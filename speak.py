from gtts import gTTS
import os
  

def speak(className):
    language = 'en'

    className+=" class started, "
    className*=3

    myobj = gTTS(text=className, lang=language, slow=False)
     
    myobj.save("className.mp3")
    
    # Playing the converted file
    os.system("className.mp3")
