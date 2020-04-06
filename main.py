from chatterbot import ChatBot

chatb = ChatBot('Alien!!')
from chatterbot.trainers import ListTrainer
from tkinter import *

import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


convo = [
    "Hello",
    "hi",

    "Hi there!",
    "what is your name?",
    "My name is CORONA , i was created by CHINA",
    "how are you?",
    "i am good i am spreading all over the world",
    "thank you",
    "in which city do you live",
    "i live in china  in wuhan city ... but now i am every where",
    "in which language do you speak",
    "i mostly talk in english "

]

trainer1 = ListTrainer(chatb)

trainer1.train(convo)

# print("TALK TO MY JAADU" )
# answer = bot.get_response("what is your name?")

# print(answer)
# while True:
#   query=input()
# if query == 'exit':
#    break
# answer=bot.get_response(query)
#     print("jaadu : ",answer)

main = Tk()

main.geometry("500x700")

main.title("corona")
photo = PhotoImage(file="g.png")
photoL = Label(main, image=photo)
photoL.pack(pady=5)


# take query audio as input
def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language="eng-in")
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("voice not recognized")



def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatb.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "Corona : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="ask corona", font=("Verdana", 20), command=ask_from_bot)

btn.pack()


# creating function

def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
