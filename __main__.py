#!/usr/bin/env python3
import json
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

import apiai
import speech_recognition as sr
from cleverwrap import CleverWrap
import core as C


import modules as M

CLIENT_ACCESS_TOKEN = '0be9930a8de146deb3014346c5de1d9d'
#Instanciar API.AI
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
#Instanciar Cleverbot
cw = CleverWrap("CC1yyLsWicOuwBwEhMJigtOkixg")

AL = M.Analyzer()


app = Flask(__name__)
api = Api(app)

TOKENS = ['234234123123eddjhskdasa342','1233543jkk4hkjdhsfhsas']

def APIAI_rec(texto):
    request = ai.text_request()
    request.lang = 'es'  # Lenguaje
    request.session_id = "_HOlaMundo_"
    request.query = texto
    response = request.getresponse()
    res = response.read()
    res = json.loads(res)
    datares = {
        'action': res['result']['action'],
        'message': res['result']['fulfillment']['messages'][0]['speech'],
        'parameters': res['result']['parameters']
        }
    return datares
def CheckToken(token):
    if token in TOKENS:
        return True
    else:
        return False
class MyIA(Resource):
    def get(self, token, frase):
        res = APIAI_rec(frase)
        if (res['action'] == 'input.unknown'):
            # No hay accion, usar cleverbot
            res['message'] = cw.say(frase)
        else:
            alrs = AL.analize(res)
            if (alrs):
                res['message'] = alrs[1]
        return res


api.add_resource(MyIA, '/ia/<token>/<frase>') # Route_1

if __name__ == '__main__':
     app.run(port=3000)
