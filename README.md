# ARTIFICIAL INTELLIGENCE PERSONAL ASSISTANT (AIPA)

AIPA (A.I. Personal Assistant) is Speech, Vision and IoT Based Intelligent Personal Assistant.

AIPA is a speech, vision and iot based intelligent personal assistant inspired by [JARVIS](https://www.facebook.com/notes/mark-zuckerberg/building-jarvis/10154361492931634/). The project is released under MIT license, I would love to have your help on improving AIPA, and see [CONTRIBUTING]() for more details.

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/29638027-8d5b2dd8-885e-11e7-8ea1-ec33f96ef522.png">
</p>

## Installation

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
