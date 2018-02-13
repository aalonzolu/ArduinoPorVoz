from sys import platform
import os


def whatOS():
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "darwin":
        return "osx"
    elif platform == "win32":
        return "windows"

def tts(text):
    if(whatOS()=="osx"):
        os.system("say -v Monica '" + text + "'")
    else:
        os.system("espeak -ves '"+text+"'")