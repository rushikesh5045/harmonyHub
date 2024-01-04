import json

def remove_specific_text_from_lyrics(input_file, output_file):

    with open(input_file, 'r') as file:
        data_without_ids = json.load(file)


    for item in data_without_ids:
        if "lyrics_body" in item:
            item["lyrics_body"] = item["lyrics_body"].split("\n\n******* This Lyrics is NOT for Commercial use *******\n")[0]


    with open(output_file, 'w') as output_file:
        json.dump(data_without_ids, output_file, indent=2)


input_file = './new_file_without_ids.json'
output_file = './new_file_without_specific_text.json'


remove_specific_text_from_lyrics(input_file, output_file)
