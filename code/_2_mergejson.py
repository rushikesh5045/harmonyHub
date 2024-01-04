import os
import json

def merge_json_files(folder_path, output_file):

    merged_data = []


    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)


            with open(file_path, 'r') as file:
                json_data = json.load(file)


            merged_data.append(json_data)


    with open(output_file, 'w') as output_file:
        json.dump(merged_data, output_file, indent=2)


folder_path = './complete_data_for_lyrics'
output_file = './merged.json'


merge_json_files(folder_path, output_file)
