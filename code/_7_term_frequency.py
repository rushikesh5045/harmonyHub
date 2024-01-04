import json
from nltk.tokenize import word_tokenize

def calculate_tf(input_file, output_file):

    with open(input_file, 'r') as file:
        data_without_stop_words = json.load(file)


    tf_per_document = {}


    for idx, item in enumerate(data_without_stop_words):
        if "lyrics_body" in item:

            words = word_tokenize(item["lyrics_body"].lower())


            term_frequency = {}
            total_words = len(words)

            for word in words:
                term_frequency[word] = term_frequency.get(word, 0) + 1


            term_frequency_normalized = {word: freq / total_words for word, freq in term_frequency.items()}


            tf_per_document[idx] = term_frequency_normalized


    with open(output_file, 'w') as output_file:
        json.dump(tf_per_document, output_file, indent=2)


input_file = './new_file_without_stop_words.json'
output_file = './tf_per_document.json'


calculate_tf(input_file, output_file)
