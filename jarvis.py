from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
from webcontrol import *
import sys
import os


MODELS = "jarvis models/model"



recongizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)


def create_note():
    global recongizer

    

    done = not True

    while not done:

        speaker.say("What would you like to write?")
        speaker.runAndWait()

        try:
            with speech_recognition.Microphone() as mic:

                recongizer.adjust_for_ambient_noise(mic, duration=0.2)  # type: ignore
                audio = recongizer.listen(mic)

                note = recongizer.recognize_google(audio)
                note = note.lower()    # type: ignore


            with open("notes.txt", "a") as f:
                f.write(note)
                done = True
                speaker.say("note created")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you, please try again")
            speaker.runAndWait()            
            
            
def add_todo():
    global recongizer

    speaker.say("what would you like to add")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                
                recongizer.adjust_for_ambient_noise(mic, duration=0.2)  # type: ignore
                audio = recongizer.listen(mic)

                item = recongizer.recognize_google(audio)
                item = item.lower()  # type: ignore

                with open("todos.txt", "a") as f:
                    f.write(item)
                done = True
                speaker.say(f"add {item} to your to do list")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
            speaker.say("I did not understand sorry")

def hello():
    speaker.say("what can i do for you")
    speaker.runAndWait()

def start_recording():
    pass

def end_recording():
    pass

def show_todos():
    if os.path.exists("todos.txt"):
        lines = open("todos.txt", "r").readlines()
        if not lines:
            speaker.say("there are no items on your to do list")
            speaker.runAndWait()
            return
        speaker.say("the items on your to do list are")
        for line in lines:
            speaker.say(line)
        speaker.runAndWait()
    else:
        speaker.say("There are no items on your to do list")
        speaker.runAndWait()

def leave():
    speaker.say("goodbye sir")
    speaker.runAndWait()
    # os.system("shutdown /s /t 0")

mappings = {"greeting": hello, "create_note": create_note, "add_todo":add_todo, "show_todos": show_todos, "exit": leave, "start_record":start_recording, "end_record":end_recording, "click_history":commandHistory}
start()
assistant = GenericAssistant('intents.json', intent_methods=mappings)

# if os.path.exists("jarvis models/model.h5") and os.path.exists("jarvis models/model_words.pkl") and os.path.exists("jarvis models/model_classes.pkl"):
#     assistant.load_model(MODELS)
# else:
assistant.train_model()
assistant.save_model(MODELS)




speaker.say("Hello Sir!")
speaker.runAndWait()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recongizer.adjust_for_ambient_noise(mic, duration=0.2)  # type: ignore
            audio = recongizer.listen(mic)


            message = recongizer.recognize_google(audio)
            message = message.lower()  # type: ignore

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recongizer = speech_recognition.Recognizer()