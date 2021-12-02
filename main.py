import speech_recognition as sr
import keyboard

r = sr.Recognizer()
mic = False
if(mic):
    filename = "machine-learning_speech-recognition_16-122828-0002.wav"
    # initialize the recognizer
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
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
