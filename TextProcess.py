#   Last Updated   - $12/9/2021$
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
            "focused", "team", "team player", "leader", "experienced", "excited", "creative", "hardworking", "driven", 
            "computer", "science", "school", "computer science", "university", "college", "creative", "hardworking",
            "driven", "opportunity", "respect", "skills", "goals", "team", "knowledge", "weakness", "confident",
            "dream", "goal", "confidence", "opportunities", "role", "growth", "aspirations", "ambition", "ambitions",
            "align", "aligns", "success", "quality", "qualities", "accomplishment", "accomplish", "accomplishments",
            "excel", "manage", "motivated", "motivations", "motivates", "motivate", "grow", "bring", "enthusiasm",
            "enthusiastic", "passion", "passionate", "passions", "work", "working", "communicate", "communication",
            "flexible", "proactive", "talent", "talented", "knowledgeable", "reliable", "position", "achievement",
            "achievements", "relevant", "relevance", "overcome", "focus", "focused", "creative", "precise",
            "detailed", "contribute", "qualified", "qualifications"]

def getFile():
    #mp4File = GET REQUEST HERE TO GET THE MP4 FILE
    mp4File = "TestFiles\\badAnswer.mp4"

    #GET THE USERID TO CREATE NEW FILES
    global userID
    userID = 1

    return mp4File

def convertToWav(mp4File):
    #convert MP4 to WAV File
    clip = mp.VideoFileClip(mp4File)
    clip.audio.write_audiofile("Convert.wav", codec='pcm_s16le')

    return "Convert.wav"

def convertToText(filename):
    #convert WAV file to text using speech_recognition
    global r
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def sendToBot(text):
    #SEND OUT TEXT FILE IF INTERVIEW IS COMPLETE USING PUT REQUEST 
    print("---SEND TO WEB NEEDS IMPLEMENTATION---")

def correctnessScore(text):
    #outputs a confidence rating to the interview question
    count = 0
    words = text.split()
    for word in words:
        if word.lower() in keywords:
            count += 1

    return (count/(len(words)))

def writeToFile(text, score, userNum):
    #writes text to the txt file
    file = open("SpeechToText" + str(userNum) + ".txt", "a+")
    file.write(str(text))
    file.write("\nConfidence: " + str(score))
    file.write("\n")
    file.close()

def removeFiles(wavFile, mp4File):
    #removes .wav and .mp4 files from computer
    os.remove(wavFile)
    #os.remove(mp4File)

def main():
    mp4File = getFile()
    wavFile = convertToWav(mp4File)
    text = convertToText(wavFile)
    score = correctnessScore(text)
    sendToBot(text)
    writeToFile(text, score, userID)
    removeFiles(wavFile, mp4File)

if __name__ == '__main__':
    main()