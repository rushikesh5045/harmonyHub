import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('stopwords')
nltk.download('punkt')

def create_word_index(input_file, output_file):

    with open(input_file, 'r') as file:
        data_without_specific_text = json.load(file)


    stop_words = set(stopwords.words('english'))


    word_index = {}


    for idx, item in enumerate(data_without_specific_text):
        if "lyrics_body" in item:

            words = word_tokenize(item["lyrics_body"].lower())


            filtered_words = [word for word in words if word not in stop_words]


            for word in filtered_words:
                if word not in word_index:
                    word_index[word] = {idx: 1}
                else:
                    if idx in word_index[word]:
                        word_index[word][idx] += 1
                    else:
                        word_index[word][idx] = 1


    with open(output_file, 'w') as output_file:
        json.dump(word_index, output_file, indent=2)


input_file = './new_file_without_stop_words.json'
output_file = './word_index.json'


create_word_index(input_file, output_file)
