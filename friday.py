# Subprocess:- This module is used for getting system subprocess details which are used in various commands. 
# Shutdown, Sleep, etc. This module comes built-in with Python.
import subprocess

# WolframAlpha:- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI 
# technology. To install this module type the below command in the terminal.
import wolframalpha

# Pyttsx3:- This module is used for the conversion of text to speech in a program it works offline.
# To install this module type the below command in the terminal. "pip install pyttsx3"
import pyttsx3

#Tkinter:- This module is used for building GUI and comes inbuilt with Python. This module comes built-in with Python. 
import tkinter


import json

# In my testing code I heavily rely on stable random generator results and it makes porting code to Python 3 a lot harder,
# if all those tests have to be adjusted. This package fixes that.
import random
import operator

# Speech Recognition:- Since we’re building an Application of voice assistant, one of the most important things in this is 
# that your assistant recognizes your voice (means what you want to say/ ask). To install this module type the below command in the terminal.
# "pip install SpeechRecognition"
import speech_recognition as sr


# Show datetime in your device
# Datetime:- Date and Time is used to showing Date and Time. This module comes built-int with Python. 
import datetime

# Wikipedia:- As we all know Wikipedia is a great source of knowledge just like GeeksforGeeks we have used 
# the Wikipedia module to get information from Wikipedia or to perform a Wikipedia search. To install this module type 
# the below command in the terminal. "pip install wikipedia"
import wikipedia

#Web browser:- To perform Web Search. This module comes built-in with Python. 
import webbrowser
import os
import winshell

# Pyjokes:- Pyjokes is used for collection Python Jokes over the Internet. To install this module type the below command in the terminal.
# "pip install pyjokes"
import pyjokes
import feedparser
import smtplib
import ctypes
import time

# Requests: Requests is used for making GET and POST requests. To install this module type the below command in the terminal.
# pip install requests 
import requests
import shutil

# Twilio:- Twilio is used for making call and messages. To install this module type the below command in the terminal.
# pip install twilio
import twilio
import progress
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("I am Friday")
	speak("I am your personal Assistant")
	speak(assname)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Akash Sir")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("---------------------------".center(columns))
	print("Welcome Akash Sir.", uname.center(columns))
	print("---------------------------".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()




if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()
	wishMe()
	username()
	while True:
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia.....')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif "open google" in query:
			speak("Here you go google\n")
			webbrowser.open("google.com")

		elif "open youtube" in query:
			speak("Here you go Youtube\n")
			webbrowser.open("youtube.com")

		elif "What is the Time" in query:
			strTime = datetime.datetime.now().strtime("% H:% M:% S")
			speak(f"akash, the time is {strTime}")

		elif "how are you" in query:
			speak("I am fine")
			speak("How are you akash?")

		elif "who are you" in query:
			speak("I am your assistant created by you.")

		elif "lock window" in query:
			speak("locking your Private System")
			ctypes.windll.user32.LockWorkStation()