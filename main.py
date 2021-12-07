import speech_recognition as sr
import moviepy.editor as mp
import keyboard
import os

keywords = ["andre", "mp4", "converter",  "test"]

r = sr.Recognizer()
count = 0
fileInput = True
mp4File = "BroadcastTest.mp4"
if(fileInput):

    clip = mp.VideoFileClip(mp4File)
    clip.audio.write_audiofile("BroadcastTestConv.wav", codec='pcm_s16le')

    filename = "BroadcastTestConv.wav"

    # initialize the recognizer
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)

        words = text.split()
        for word in words:
            if word.lower() in keywords:
                count += 1
        print(count/(len(words)))

        file = open("SpeechToText.txt", "a+")
        file.write(text)
        file.write("\n")
        file.close()

    os.remove(filename)
    #os.remove(mp4File)
else:
    print("speak anything: ")
    try:
        while(True):
            with sr.Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
    except KeyboardInterrupt:
        pass

