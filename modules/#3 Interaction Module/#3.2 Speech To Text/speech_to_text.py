#-----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# date        : 19.08.2017
#-----------------------------------------

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os # to execute commands

def main():
	# obtain audio from the microphone
	while True:
	    r = sr.Recognizer()
	    with sr.Microphone() as source:
		print("listening...")		
		audio = r.listen(source)
		print("sa")
	    # recognize speech using Google Speech Recognition
	    try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		print("as")		
		command = r.recognize_google(audio)
		print("You said: " + command)
		
	    #exception handling
	    except sr.UnknownValueError:
		print("I could not understand audio")
	    except sr.RequestError as e:
		print("Could not request results from Speech Recognition service; {0}".format(e))	        

main()
