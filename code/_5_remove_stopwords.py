import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(input_file, output_file):

    with open(input_file, 'r') as file:
        data_without_specific_text = json.load(file)


    stop_words = set(stopwords.words('english'))


    for index, item in enumerate(data_without_specific_text):
        if "lyrics_body" in item:

            words = word_tokenize(item["lyrics_body"])
            

            filtered_words = [word for word in words if word.lower() not in stop_words]
            

            filtered_lyrics = ' '.join(filtered_words).replace('...', '')
            

            item["lyrics_body"] = filtered_lyrics.strip()
            

            item["document_number"] = index


    with open(output_file, 'w') as output_file:
        json.dump(data_without_specific_text, output_file, indent=2)


input_file = './new_file_without_specific_text.json'
output_file = './new_file_without_stop_words.json'


remove_stop_words(input_file, output_file)
