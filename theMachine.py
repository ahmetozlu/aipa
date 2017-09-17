#-----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# start date  : 19.08.2017
#-----------------------------------------

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import sys # to terminate the program
import time # to get current datetime
import os # to execute commands

# a function to char by char print out
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

# obtain audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print1by1("What are your commands?")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
	command = r.recognize_google(audio)
        print1by1("You said: " + command)

	# the default defined commands
        if(command == "who am I"):
            print1by1("Admin")
	elif(command == "who are you"):
	    print1by1("I am the machine which makes human life easier!")
	elif(command == "what time is it"):
	    time.ctime()
	    print1by1(time.strftime('%l:%M%p %Z on %b %d, %Y'))	
	elif(command == "okay the machine goodbye"):
	    print1by1("goodbye!")
	    sys.exit()
	elif(command == "open file manager"):
	    os.system("xdg-open /home/ahmetozlu/Desktop")

    #exception handling
    except sr.UnknownValueError:
        print1by1("I could not understand audio")
    except sr.RequestError as e:
        print1by1("Could not request results from Speech Recognition service; {0}".format(e))
