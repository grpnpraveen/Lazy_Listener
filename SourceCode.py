from playsound import playsound
import pyttsx3
import urllib.error,urllib.parse,urllib.request
import requests
from bs4 import BeautifulSoup
import os
further='y'
                                        #  Defining  Function  to speak
def assistanat():
    fhand=open(r"username.txt",'r')
    mastername=fhand.read()

    if mastername=='none':
        master=pyttsx3.init()
        master.say("Enter user name")
        master.runAndWait()
        mastername=input("Enter user name :) -")
        fhand=open(r"username.txt",'w')
        y=fhand.write(mastername)
        master=pyttsx3.init()
        master.say("welcome                    master")
        master.say(mastername)
        master.say("   NICE TO feel you")
        master.runAndWait()
    else:
        master=pyttsx3.init()
        master.say("welcome                    master")
        master.say(mastername)
        master.say("   NICE TO feel you")
        master.runAndWait()
    master=pyttsx3.init()
    master.say("choose your option")
    master.runAndWait()
    print("\nChoose your option",mastername,end=":)-\n")#asking user choice of reading file
    print("\n1.LOCAL FILE\n2.ONLINE ")
    optionselection=int(input("ENTER YOUR CHOICE:) -  "))
    if optionselection==2:
        master=pyttsx3.init()
        master.say("ENTER      THE   URL     YOU       WANT      ME         TO      READ         FOR        YOU:")
        master.runAndWait()
        filewanttoread=input("ENTER THE URL  YOU WANT ME TO READ FOR YOU :)-")
                #   http://data.pr4e.org/romeo.txt
        html=urllib.request.urlopen(filewanttoread).read()
        soup=BeautifulSoup(html,'html.parser')
        speaker=pyttsx3.init()
        print(soup)
        speaker.say(soup)
        speaker.runAndWait()

    else:
        path=input("Enter the path of the file:")
        fhand=open(path,"r")
        y=fhand.read()
        speaker=pyttsx3.init()
        speaker.say(y)
        speaker.save_to_file(y , 'History.mp3')
        speaker.runAndWait()



            #                                      Main    PROGRAM   RUNS FROM HERE
master=pyttsx3.init()
master.say("hey welcome to lazy listener, Select the voice")
master.runAndWait()
while further=='y' or further=='Y':
    print("----------Select the options-------either(1 or 2)----")
    voice=int(input("1.Male\n2.Female\n:)-"))

    if voice==1:
        mastername=pyttsx3.init()
        voices = mastername.getProperty('voices')
        mastername.setProperty('voice', voices[0].id)
        assistanat()

    else:
        mastername=pyttsx3.init()
        voices = mastername.getProperty('voices')
        mastername.setProperty('voice', voices[1].id)
        assistanat()
    master=pyttsx3.init()
    master.say("want you to assist again")
    master.runAndWait()
    further=input("Want to assist again  (y or n) :)-")
    os.system('cls')
playsound("off.mp3")
