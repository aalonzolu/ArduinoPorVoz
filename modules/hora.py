# -*- coding: utf-8 -*-
import time


class Hora:
    def __init__(self):
        self.action = ["say-hour"]

    def getAction(self,):
        return self.action

    def analizar(self,data):
        if(data['action']=='say-hour'):
            hora = time.strftime("La hora es %H horas con %M minutos")
            print(hora)
        else:
            hora = "Error en hora"
        return [True, hora]