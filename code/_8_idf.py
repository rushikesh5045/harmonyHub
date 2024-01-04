import json
import math

def calculate_idf(word_index_file, total_documents, output_file):

    with open(word_index_file, 'r') as file:
        word_index = json.load(file)


    idf_per_word = {}


    for word, doc_info in word_index.items():
        df = len(doc_info)  
        idf = math.log(total_documents / df)
        idf_per_word[word] = idf


    with open(output_file, 'w') as output_file:
        json.dump(idf_per_word, output_file, indent=2)


word_index_file = './word_index.json'
total_documents = 33266  
output_file = './idf_per_word.json'


calculate_idf(word_index_file, total_documents, output_file)
