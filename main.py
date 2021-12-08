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

keywords = ["My name is", "student", "years", "experience", "field", "engaged", "creative", "hardworking", "driven", 
            "focused", "team", "team player", "experience", "field", "engaged", "creative", "hardworking", "driven", 
            "My name is", "student", "years", "experience", "field", "engaged", "creative", "hardworking", "driven", 
            "My name is", "student", "years", "experience", "field", "engaged", "creative", "hardworking", "driven", 
            "My name is", "student", "years", "experience", "field", "engaged", "creative", "hardworking", "driven", ]

# initialize the recognizer
r = sr.Recognizer()

def getFile():
    #mp4File = GET REQUEST HERE TO GET THE MP4 FILE
    mp4File = "BroadcastTest.mp4"

    #GET THE USERID TO CREATE NEW FILES
    global userID
    userID = 1

    clip = mp.VideoFileClip(mp4File)
    clip.audio.write_audiofile("Convert.wav", codec='pcm_s16le')

    return "Convert.wav"

def convertToText(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

        return text

def sendToBot(text):
    print("---NEEDS IMPLEMENTATION---")


def textProcess(text):
    #outputs a confidence rating to the interview question
    count = 0
    #print(text)
    words = text.split()
    for word in words:
        if word.lower() in keywords:
            count += 1

    return (count/(len(words)))

def writeToFile(text, conf):
    #writes text to the txt file
    file = open("SpeechToText" + str(userID) + ".txt", "a+")
    file.write(str(text))
    file.write("\nConfidence: " + str(conf))
    file.write("\n")
    file.close()

def removeFiles():
    #removes .wav and .mp4 files from computer
    os.remove(wavFile)
    #os.remove(mp4File)

wavFile = getFile()
text = convertToText(wavFile)
confidence = textProcess(text)
sendToBot(text)
writeToFile(text, confidence)
removeFiles()
#SEND OUT TEXT FILE IF INTERVIEW IS COMPLETE USING PUT REQUEST 


