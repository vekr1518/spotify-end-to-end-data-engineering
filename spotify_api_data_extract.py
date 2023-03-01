import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime


def lambda_handler(event, context):
    cilent_id = os.environ.get('client_id')
    cilent_secret = os.environ.get('client_secret')

    spotify_credential = SpotifyClientCredentials(client_id=cilent_id, client_secret=cilent_secret)
    sp = spotipy.Spotify(client_credentials_manager=spotify_credential)
    ani_album_loc = "https://open.spotify.com/artist/4zCH9qm4R2DADamUHMCa6O"
    data = sp.artist_albums(ani_album_loc)

    filename = "spotify_raw_" + str(datetime.now()) + ".json"

    cilent = boto3.client('s3')
    cilent.put_object(
        Bucket='vkfirsts3bucket',
        Key="raw_data/to_process/" + filename,
        Body=json.dumps(data)
    )
