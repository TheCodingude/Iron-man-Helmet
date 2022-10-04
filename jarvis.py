from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import os

recongizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = []

def create_note():
    global recongizer

    

    done = not True

    while not done:

        speaker.say("What would you like to write?")
        speaker.runAndWait()

        try:
            with speech_recognition.Microphone() as mic:

                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen(mic)

                note = recongizer.recognize_google(audio)
                note = note.lower()


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
                
                recongizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recongizer.listen(mic)

                item = recongizer.recognize_google(audio)
                item = item.lower()

                with open("todos.txt", "a") as f:
                    f.write(item)
                done = True
                speaker.say(f"add {item} to your to do list")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recongizer = speech_recognition.Recognizer()
            speaker.say("I did not understand sorry")

def hello():
    pass

def start_recording():
    pass

def end_recording():
    pass

def show_todos():
    pass

def leave():
    pass

mappings = {"greeting": hello, "create_note": create_note, "add_todo":add_todo, "show_todos": show_todos, "exit": leave, "start_record":start_recording, "end_record":end_recording}

assistant = GenericAssistant('intents.json', intent_methods=mappings)

if os.path.exists("model.h5"):
    assistant.load_model("model")
else:
    assistant.train_model()
    assistant.save_model("model")

speaker.say("Hello Sir!")
speaker.runAndWait()


while True:

    try:
        with speech_recognition.Microphone() as mic:

            recongizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recongizer.listen(mic)


            message = recongizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recongizer = speech_recognition.Recognizer()