import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
# import pandas as pd




def get_album(search_str):
    
    client_id = '99725a253fa84f2d9a02b3636cf56350'
    client_secret = 'c774c60838fa42a5b8bcbf4be7b5d420'

    os.environ['SPOTIPY_CLIENT_ID'] = client_id
    os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # if len(sys.argv) > 1:
    #     search_str = sys.argv[1]
    # else:
    #     search_str = 

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    album = sp.search(search_str)
    
    for key in album['tracks']['items']:
        album_data = []
        album_data.append(key['name'])
        album_data.append(key['id'])
        print(album_data)
    # print(album['tracks']['items'])
    # print(type(album['tracks']['items']))



    

