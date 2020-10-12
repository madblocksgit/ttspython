from gtts import gTTS
import playsound

language='en'
text='Hey Madhu'

m=gTTS(text=text,lang=language,slow=False)
m.save('madhu.mp3')
playsound.playsound('madhu.mp3',True)
