from dotenv import load_dotenv
import speech_recognition as sr
import os
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia as wiki
import webbrowser as web

load_dotenv()

number = os.getenv("Number")
Daksh = os.getenv("Daksh")
Deepahshu = os.getenv("Deepahshu")

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return print(text)

def get_speech_input(prompt):
    with sr.Microphone() as source:
        text_to_speech(prompt)
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio_data = r.listen(source)
        text_to_speech("Recognizing....")
        try:
            text = r.recognize_google(audio_data,language='en-in')
            print("user: ",text,"\n")
            return text
        except sr.UnknownValueError:
            text_to_speech("SIR.... I COULD NOT UNDERSTAND YOU...")   
        except sr.RequestError:
            text_to_speech("SIR.... I COULD NOT CONNECT TO THE INTERNET...")
            
def execute_command(cmd):
    if "WhatsApp" in cmd:
        now = datetime.datetime.now()
        message = get_speech_input("what's your message....") 
        try:
            kit.sendwhatmsg(number, message, now.hour, now.minute + 2)
        except Exception as e:
            print(f"Failed to send message: {e}")

    elif "Wikipedia" in cmd:
        text_to_speech("searching pedia..")
        query = cmd.replace("Wikipedia","")
        results = wiki.summary(query,sentences=2)
        text_to_speech("According to pedia..")
        print(results)
        text_to_speech(results)
    
    elif "Google" in cmd:
        text_to_speech("searching..")
        query = cmd.replace("Google","").replace(" ","")
        web.open(f"https://www.{query}.com")
        if "udemy" in query:
           u_cmd = get_speech_input(f"What you like to study on {query}..")
           study = {
               "web development":"https://www.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture",
               "python":"https://www.udemy.com/course/100-days-of-code/learn/lecture"
                }
           try:
               web.open(study[u_cmd])
           except Exception as e:
               print(f"Failed to send message:{e}\n")

    elif "Instagram" in cmd:
        web.open("https://www.instagram.com/dkking5143/")
        text_to_speech("SIR.... HERE WHAT YOU..ASKED...")
        in_cmd = get_speech_input("Whom do you want to message....")
        contacts = {
                    "Daksh": Daksh,
                    "Deepahshu": Deepahshu
                    }
        try:
                web.open(contacts[in_cmd])
        except Exception as e:
                print(f"Failed to send message:{e}\n")

    elif "paint" in cmd:
        os.system(f"start {os.getenv("path")}Paint.lnk")
        text_to_speech("SIR.... HERE WHAT YOU..ASKED...")

    elif "shutdown" in cmd:
        os.system("shutdown /s")
        text_to_speech("SIR SYSTEM GOING TO SHUTDOWN IN LESS THAN MINUTE ....")
        return False
    
    elif "rest" in cmd:
        text_to_speech("GOOD DAY SIR....")
        return False

    else:
        try:
            os.system(cmd)
        except Exception as e:
            print(f"Failed: {e}\n")
    return True

r = sr.Recognizer()

agin = True

while(agin):
  text = get_speech_input("SIR what's your COMMAND....")

  if text is not None and "friday" in text.lower():
    cmd = text.replace("Friday","").replace("friday","").strip()
    agin = execute_command(cmd)

  elif text is not None and "kill" in text :
      text_to_speech("GOOD DAY SIR....")
      os.system('taskkill /IM "code.exe" /F')
