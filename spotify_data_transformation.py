import json
import boto3
import pandas as pd
from datetime import datetime
from io import StringIO


def album(data):
    album_list = []
    for row in data['items']:
        name = row['name']
        release_date = row['release_date']
        total_tracks = row['total_tracks']
        artist = row['artists'][0]['name']
        album_url = row['external_urls']['spotify']
        array_element = {'name': name, 'release_date': release_date, 'total_tracks': total_tracks, 'artist': artist,
                         'album_url': album_url}
        album_list.append(array_element)

    return album_list


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucket = "vkfirsts3bucket"
    Key = "raw_data/to_process/"

    spotify_data = []
    spotify_key = []

    for file in s3.list_objects(Bucket=Bucket, Prefix=Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1] == "json":
            response = s3.get_object(Bucket=Bucket, Key=file_key)
            content = response['Body']
            jsonObject = json.loads(content.read())
            spotify_data.append(jsonObject)
            spotify_key.append(file_key)
            # print(spotify_key)

    for data in spotify_data:
        album_list = album(data)

        ani_album_df = pd.DataFrame.from_dict(album_list)

        album_key = "transformed_data/ani_album_data/album_transformed_" + str(datetime.now()) + ".csv"
        album_buffer = StringIO()
        ani_album_df.to_csv(album_buffer, index=False)
        album_content = album_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=album_key, Body=album_content)

    s3_resource = boto3.resource('s3')
    for keys in spotify_key:
        copy_source = {
            'Bucket': Bucket,
            'Key': keys
        }
        s3_resource.meta.client.copy(copy_source, "vkfirsts3bucket", 'raw_data/processed/' + keys.split("/")[-1])
        s3_resource.Object(Bucket, keys).delete()











