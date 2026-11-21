import pyttsx3

word = input("What should i say?")

voice = pyttsx3.init()
voice.say(word)
voice.runAndWait()
