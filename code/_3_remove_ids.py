import json

def remove_ids_and_create_new_file(input_file, output_file):

    with open(input_file, 'r') as file:
        merged_data = json.load(file)


    for item in merged_data:
        if "commontrack_id" in item:
            del item["commontrack_id"]
        if "track_id" in item:
            del item["track_id"]


    with open(output_file, 'w') as output_file:
        json.dump(merged_data, output_file, indent=2)


input_file = './merged.json'
output_file = './new_file_without_ids.json'


remove_ids_and_create_new_file(input_file, output_file)

