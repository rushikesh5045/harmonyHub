import requests
import csv
import json

def get_lyrics(api_key, commontrack_id):
    base_url = "https://api.musixmatch.com/ws/1.1/"
    track_info_endpoint = "track.get"
    lyrics_endpoint = "track.lyrics.get"


    track_id = get_track_id(api_key, commontrack_id)

    if track_id:

        artist_name, song_name = get_track_info(api_key, track_id)

        if artist_name is not None and song_name is not None:
            print(f"Track ID {track_id} belongs to Artist: {artist_name}, Song: {song_name}")


            lyrics_body = get_lyrics_body(api_key, commontrack_id, track_id)

            if lyrics_body:

                output_filename = f"lyrics_{commontrack_id}_{track_id}.json"
                output_filepath = f"./output_lyrics_2/{output_filename}"

                with open(output_filepath, 'w') as output_json:
                    json.dump({
                        'commontrack_id': commontrack_id,
                        'track_id': track_id,
                        'artist_name': artist_name,
                        'song_name': song_name,
                        'lyrics_body': lyrics_body
                    }, output_json)

                print(f"Lyrics for commontrack_id {commontrack_id} and track_id {track_id} stored in {output_filepath}.")
            else:
                print(f"Failed to fetch lyrics for commontrack_id {commontrack_id} and track_id {track_id}.")
        else:
            print(f"Failed to fetch track info for Track ID {track_id}.")

def get_track_id(api_key, commontrack_id):
    base_url = "https://api.musixmatch.com/ws/1.1/"
    endpoint = "track.get"

    params = {
        'apikey': api_key,
        'commontrack_id': commontrack_id,
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)

    if response.status_code == 200:
        data = response.json()


        if 'track' in data['message']['body'] and data['message']['body']['track']['has_lyrics'] == 1:
            return data['message']['body']['track']['track_id']
        else:
            return None
    else:
        return None

def get_track_info(api_key, track_id):
    base_url = "https://api.musixmatch.com/ws/1.1/"
    endpoint = "track.get"

    params = {
        'apikey': api_key,
        'track_id': track_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)

    if response.status_code == 200:
        data = response.json()
        status_code = data.get('message', {}).get('header', {}).get('status_code', None)

        if status_code == 200:
            track_info = data.get('message', {}).get('body', {}).get('track', {})
            artist_name = track_info.get('artist_name', None)
            song_name = track_info.get('track_name', None)

            return artist_name, song_name
        else:
            print(f"Musixmatch API returned a non-success status code: {status_code}")
    else:
        print(f"Failed to fetch track info. HTTP status code: {response.status_code}")
    return None, None

def get_lyrics_body(api_key, commontrack_id, track_id):
    base_url = "https://api.musixmatch.com/ws/1.1/"
    endpoint = "track.lyrics.get"

    params = {
        'apikey': api_key,
        'commontrack_id': commontrack_id,
        'track_id': track_id
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)

    if response.status_code == 200:
        data = response.json()
        status_code = data.get('message', {}).get('header', {}).get('status_code', None)

        if status_code == 200:
            return data.get('message', {}).get('body', {}).get('lyrics', {}).get('lyrics_body', None)
        else:
            print(f"Musixmatch API returned a non-success status code: {status_code}")
    else:
        print(f"Failed to fetch lyrics. HTTP status code: {response.status_code}")
        return None


api_key = 'ac6a5c2cfd13d50baddc4aadd83831ca'


for commontrack_id in range(8000, 18000):
    get_lyrics(api_key, commontrack_id)

print("Script execution completed.")
