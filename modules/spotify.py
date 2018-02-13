# -*- coding: utf-8 -*-
import spotipy
spotify = spotipy.Spotify()

class SpotiPy:
    def __init__(self):
        self.action = ["play-music" , "stop-music"]

    def getAction(self,):
        return self.action

    def analizar(self,data):
        res = ""
        print("Spotiy analizer")
        print (data)
        if(data['action']=='play-music'):
            if data['parameters']['artist'] != "":
                print ("Buscando artista ", data['parameters']['artist'])
                results = spotify.search(q='artist:' + data['parameters']['artits'], type='artist')
                items = results['artists']['items']
                if len(items) > 0:
                    artist = items[0]
                    print(artist['name'], artist['images'][0]['url'])
        return False