# ARTIFICIAL INTELLIGENCE PERSONAL ASSISTANT (AIPA)

AIPA (A.I. Personal Assistant) is Speech, Vision and IoT Based Intelligent Personal Assistant.

AIPA is a speech, vision and iot based intelligent personal assistant inspired by [JARVIS](https://www.facebook.com/notes/mark-zuckerberg/building-jarvis/10154361492931634/). The project is released under MIT license, I would love to have your help on improving AIPA, and see [CONTRIBUTING]() for more details.

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/29638027-8d5b2dd8-885e-11e7-8ea1-ec33f96ef522.png">
</p>

## THEORY

### System Design

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/30514270-2bbcd350-9b1a-11e7-94e6-066eeb149a7f.png">
</p>

Here are 4 main modules in AIPA;

### 1.) Security Module

Security Module has 2 layers to provide high secure system. First layer is traditionalUSerName-Password Authentication, the second layer is Multi-View Face Recognition Authentication.

   **a.)** [UserName-Password Authentication](https://github.com/ahmetozlu/aipa/tree/master/modules/%231%20UserName%20-%20Password%20Authentication): It is traditional login system. You should set the username and password for user types, and there are 2 types for users which are *ADMIN* and *GUEST*. *ADMIN* has full access of the AIPA abilities but *GUEST* has restricted access of the APIA abilities. User has to enter right UserName-Password to pass the first security layer. After the passing for the UserName-Password Authentication, Face Recognition Authentication will be started.

   **b.)** [Multi-View Face Recognition Authentication](https://github.com/ahmetozlu/aipa/tree/master/modules/%232%20Face%20Recognition%20Authentication): It is security system which is Face Recognition based. It is **multi-view face recognition** system so it provides so high security. User who claims that I am *ADMIN* have to proof it via showing his/her face for approximately 10 seconds the web camera to proof that he/she is *ADMIN*. The accuracy of this recognition system above than 97% right now, and the developing of the accuracy is in progress.


<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/30519214-d8884582-9b98-11e7-8e7e-03d279db203d.jpg">
</p>


### 2.) [Brain Module](https://github.com/ahmetozlu/aipa/tree/master/modules/%234%20Modelling%20Contextual%20Chatbot%20(with%20TensorFlow))

Brain Module is the coolest part of this AI application. In this module, AIPA learn new things from its experiences and what you teach. The more context an AI has, the better it can handle open-ended requests so AIPA tries to learn new things every time. AIPA reacts accross the users requestments by using it's knowledge. The stateless system (i.e. AIPA can remember what the user said and respond accordingly) is provided using this Brain Module.

Only *ADMIN* can teach to AIPA by speaking or entering text as his/her choise. This module is based Machine Learning and it was developed via [TensorFlow](https://www.tensorflow.org/).

Brain Module designed through 3 steps:

 1. I transformed conversational intent definitions to a Tensorflow model

 2. Next, I built a chatbot framework to process responses

 3. Lastly, I showed how basic context can be incorporated into our response processor



### 3.) [Interaction Module](https://github.com/ahmetozlu/aipa/tree/master/modules/%233%20Speech%20To%20Text)

Interaction Module consists of the Human-Computer Interaction systems. It has Speech Recognition so users can have communicate with AIPA or command their requestmens via speaking. Moreover, it also has Messenger Bot so users can have communicate with AIPA or command via entering text.



### 4.) IoT Module

*ADMIN* can manage home remotely or onsite;

 1. Turn on/off the lights
 
 2. See who is ringing the bell
 
 3. Check the rooms temperature 
 
 4. Run the air conditions

This module provides the home automation, and it uses a light-weighted protocol which is [MQTT](http://mqtt.org/).



## SYSTEM REQUIREMENTS

 Operating Systems           | Linux                           
 :--- | :--- |
 **Languages**               | **English**
 **System Requirements**     | **Minimally 1 core , 3GB free RAM**



## INSTALLATION

**1.) Python and pip**

Python is automatically installed on Ubuntu. Take a moment to confirm (by issuing a python -V command) that one of the following Python versions is already installed on your system:


- Python 2.7
- Python 3.3+

The pip or pip3 package manager is usually installed on Ubuntu. Take a moment to confirm (by issuing a *pip -V* or *pip3 -V* command) that pip or pip3 is installed. We strongly recommend version 8.1 or higher of pip or pip3. If Version 8.1 or later is not installed, issue the following command, which will either install or upgrade to the latest pip version:

    $ sudo apt-get install python-pip python-dev   # for Python 2.7
    $ sudo apt-get install python3-pip python3-dev # for Python 3.n
    
    
**2.) SpeechRecognition 2.1.3**

    pip install SpeechRecognition

**3.) face_recognition 0.1.6**

You can install this module from pypi using pip3 (or pip2 for Python 2):

    $ pip3 install face_recognition

It’s very likely that you will run into problems when pip tries to compile the dlib dependency. If that happens, check out this guide to installing dlib from source instead to fix the error:

[How to install dlib from source](#dlib)

After manually installing dlib, try running pip3 install face_recognition again.


**3.) Tensorflow**

Install TensorFlow by invoking one of the following commands:

    $ pip install tensorflow      # Python 2.7; CPU support (no GPU support)
    $ pip3 install tensorflow     # Python 3.n; CPU support (no GPU support)
    $ pip install tensorflow-gpu  # Python 2.7;  GPU support
    $ pip3 install tensorflow-gpu # Python 3.n; GPU support
    
    
<a name="dlib"/>

**4.) dlib**

Install dlib prerequisites

The dlib library only has four primary prerequisites:
Boost
Boost.Python
CMake
X11/XQuartx

Installing CMake, Boost, Boost.Python, and X11 can be accomplished easily with  **apt-get** :

    $ sudo apt-get install build-essential cmake
    $ sudo apt-get install libgtk-3-dev
    $ sudo apt-get install libboost-all-dev
    
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python get-pip.py
    
Install dlib with Python bindings

The dlib library doesn’t have any real Python prerequisites, but if you plan on using dlib for any type of computer vision or image processing, I would recommend installing:


- NumPy
- SciPy
- scikit-image

These packages can be installed via pip :

    $ pip install numpy
    $ pip install scipy
    $ pip install scikit-image
    
Years ago, we had to compile dlib manually from source (similar to how we install OpenCV). However, we can now use pip  to install dlib as well:

    $ pip install dlib
