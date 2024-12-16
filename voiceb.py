import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # Fix: Changed recognize_goggle to recognize_google
            instruction = instruction.lower()
            if "dude" in instruction:
                instruction = instruction.replace('dude', ' ')  # Fix: Typo in variable name
                print(instruction)
    except:
        pass
    return instruction

def play_dude():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing " + song)
        pywhatkit.playonyt(song)  # Fix: Changed playsong to playonyt

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')  # Fix: Added space before %p for proper formatting
        talk('Current time is ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')  # Fix: Removed spaces before and after '/'
        talk("Today's date is " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')

    elif 'what is your name' in instruction:
        talk('I am dude. What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk('Please repeat')

play_dude()