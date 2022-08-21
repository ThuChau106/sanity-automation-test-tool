from gtts import gTTS
import os
import playsound

# Function to transfer text to speech
def speak(text): 
    tts = gTTS(text=text, lang='en', slow=False)
    filename = "voiceFile.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)