import speech_recognition as sr
import moviepy.editor as mp
import keyboard

r = sr.Recognizer()
mic = True
if(mic):

    clip = mp.VideoFileClip("BroadcastTest.mp4")
    clip.audio.write_audiofile("BroadcastTestConv.wav", codec='pcm_s16le')

    filename = "BroadcastTestConv.wav"

    # initialize the recognizer
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)

        file = open("SpeechToText.txt", "w")
        file.write(text)
        file.close()
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

