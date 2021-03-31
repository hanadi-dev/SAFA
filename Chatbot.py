import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
#import pyautogui #screenshot
import pyttsx3
#import bs4 as bs
import urllib.request
import requests
import Adafruit_BBIO.GPIO as GPIO #for the hardware
from Adafruit_IO import  #for the hardware
 import Adafruit_BBIO.ADC as ADC #for the sensor

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}. what's your name?") #incase you haven't provided your name.

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
        
        
    #tempreture
    if there_exists(["what's the temperature","tell me the temperature","temperature"]):
        ADC.setup()
        temp=ADC.read("P9_40")

        engine_speak("the temperature is"+ temp)
        
    #cleaning
    if there_exists(["Start cleaning robot","start cleaning please","cleaning please","clean"]):
        engine_speak("the cleaning process is started")
        Client, Feed, RequestError KEY='2d8515d8dfe140adb0ca8f8fcdcf66cd' 
        USERNAME='abubakarstan' aio = Client(USERNAME, KEY) solar = aio.feeds("solar") operation = aio.feeds("operation") 
        GPIO.setup("P8_13",GPIO.OUT) GPIO.setup("P8_19",GPIO.OUT) 
        GPIO.setup("P9_14",GPIO.OUT) GPIO.setup("P9_16",GPIO.OUT) 

        while True:
            data = aio.receive(solar.key)
            if int(data.value) ==1:
                 print('-------Operation Started-------')
                 GPIO.output("P8_13",GPIO.LOW)
                 print("Cleaing MOTORs started -Going down-")
                 time.sleep(30)
                 GPIO.output("P8_13",GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(5)
                 GPIO.output("P8_19",GPIO.LOW)
                 print("Cleaing MOTORs started -Going up-")
                 time.sleep(30)
                 GPIO.output("P8_19", GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(5)
                 GPIO.output("P9_14",GPIO.LOW)
                 print("Dragging MOTOR Started")
                 time.sleep(30)
                 GPIO.output("P9_14", GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(3)
                 GPIO.output("P8_13",GPIO.LOW)
                 print("Cleaing MOTORs started -Going down-")
                 time.sleep(30)
                 GPIO.output("P8_13",GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(5)
                 GPIO.output("P8_19",GPIO.LOW)
                 print("Cleaing MOTORs started -going up-")
                 time.sleep(30)
                 GPIO.output("P8_19", GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(5)
                 GPIO.output("P9_16",GPIO.LOW)
                 print("Dragging MOTOR started")
                 time.sleep(30)
                 GPIO.output("P9_16", GPIO.HIGH)
                 print("MOTOR Stops")
                 time.sleep(5)
                 waiting = 0
                 print('Mission Completed, Waiting for Next Operation', waiting)
                 aio.send(solar.key, waiting)
                 time.sleep(1)


    
    
      
      #9 dashboard
    if there_exists(["dashboard"]):
        search_term = voice_data.split("for")[-1]
        url = "D:/python/admin/xtreme-html/ltr/table-basic.html"
        webbrowser.get().open(url)
        engine_speak("Here is the dashboard")

   



    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye")
        exit()



time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Safa'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("How can I help you?") # get the voice input
    print("Done")
    print("Employee:", voice_data)
    respond(voice_data) # respond