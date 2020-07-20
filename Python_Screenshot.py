import speech_recognition as sr
import time
import pyautogui
t=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Screenshot:")
    aud= t.listen(source)
    try:
        txt=t.recognize_google(aud)
        print("You said : {}".format(txt))
    except:
        print("Sorry could not hear anything")

for i in txt:
    if i.isdigit():
        sec=i
        sec=int(sec)
if "screenshot" in txt.lower():
    time.sleep(sec)
    pyautogui.screenshot("Screenshot 2.png")
