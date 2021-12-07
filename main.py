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

class TextualAnalysis():
    r = sr.Recognizer()
    count = 0
    mp4File = "BroadcastTest.mp4"
    #mp4File = GET REQUEST HERE TO GET THE MP4 FILE

    #GET THE USERID TO CREATE NEW FILES
    userID = 1

    clip = mp.VideoFileClip(mp4File)
    clip.audio.write_audiofile("BroadcastTestConv.wav", codec='pcm_s16le')

    filename = "BroadcastTestConv.wav"

    # initialize the recognizer
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
        #POST REQUEST TO SEND THE STRING TO THE BOT

        words = text.split()
        for word in words:
            if word.lower() in keywords:
                count += 1
        print(count/(len(words)))

        file = open("SpeechToText" + str(userID) + ".txt", "a+")
        file.write(text)
        file.write("\n")
        file.close()

    os.remove(filename)
    #os.remove(mp4File)

    #SEND OUT TEXT FILE IF INTERVIEW IS COMPLETE USING PUT REQUEST
