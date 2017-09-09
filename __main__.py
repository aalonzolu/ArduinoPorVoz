#!/usr/bin/env python3

import speech_recognition as sr
from gtts import gTTS
import json
import apiai
from playsound import playsound


import arduino

CLIENT_ACCESS_TOKEN = '0be9930a8de146deb3014346c5de1d9d'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
request = ai.text_request()
request.lang = 'es'  # Lenguaje
request.session_id = "_HOlaMundo_"


def APIAI_rec(texto):
    request = ai.text_request()
    request.lang = 'es'  # Lenguaje
    request.session_id = "_HOlaMundo_"
    request.query = texto
    response = request.getresponse()
    res = response.read()
    res = json.loads(res)
    return {'action':res['result']['action'],'message':res['result']['fulfillment']['messages'][0]['speech']}

Running = True
#audio from mic
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
while Running:
    print()
    #r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    with sr.Microphone() as source:
        print("Diga algo: ")
        audio = r.listen(source)
    try:
        frase = r.recognize_google(audio,language="es-GT")
        print("Usted dijo: " + frase)
        res = APIAI_rec(frase)
        arduino.arduAction(res['action'])
        print(res['message'])
        tts = gTTS(text=res['message'], lang='es')
        tts.save("say.mp3")
        playsound("./say.mp3")
        print()
    except:
        print("No se le entiende nada")
    if frase.lower() == "salir":
        Running = False
