#   Last Updated   - $12/7/2021$
#   Updated By     - $Andre$
#   Python Version - 3.8.8
"""
    GET MP4 files from Web Services. Convert MP4 to text. Send it back to Web Services
    while creating a transcript and analyzing correctness.

"""

import speech_recognition as sr
import moviepy.editor as mp
import keyboard
import os

keywords = ["My name is", "student", "years", "experience", "", "", "", "", "",]
r = sr.Recognizer()

def TextProcess(text):
    #outputs a confidence rating to the interview question
    count = 0
    print(text)
    words = text.split()
    for word in words:
        if word.lower() in keywords:
            count += 1
    print(count/(len(words)))

def writeToFile(text):
    #writes text to the txt file
    file = open("SpeechToText" + str(userID) + ".txt", "a+")
    file.write(text)
    file.write("\n")
    file.close()

def removeFiles():
    #removes .wav and .mp4 files from computer
    os.remove(filename)
    #os.remove(mp4File)

#mp4File = GET REQUEST HERE TO GET THE MP4 FILE
mp4File = "BroadcastTest.mp4"

#GET THE USERID TO CREATE NEW FILES
userID = 1

clip = mp.VideoFileClip(mp4File)
clip.audio.write_audiofile("Convert.wav", codec='pcm_s16le')

filename = "Convert.wav"

# initialize the recognizer
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    #POST REQUEST TO SEND THE STRING TO THE BOT
    TextProcess(text)
    writeToFile(text)

removeFiles()
#SEND OUT TEXT FILE IF INTERVIEW IS COMPLETE USING PUT REQUEST 

