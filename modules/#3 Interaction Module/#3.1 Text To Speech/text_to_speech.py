from gtts import gTTS
import os

def textToSpeechFunction( str ):
	tts = gTTS(text=str, lang='en')
	tts.save("pcvoice.mp3")
	# this is for linux
	os.system("mpg321 pcvoice.mp3")

textToSpeechFunction( "hello" )
