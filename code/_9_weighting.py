import json
import math

def calculate_tfidf(tf_file, idf_file, output_file):

    with open(tf_file, 'r') as file:
        tf_per_document = json.load(file)


    with open(idf_file, 'r') as file:
        idf_per_word = json.load(file)


    tfidf_per_word = {}


    for document_number, term_frequency in tf_per_document.items():
        for word, tf in term_frequency.items():
            if word not in tfidf_per_word:
                tfidf_per_word[word] = {document_number: tf * idf_per_word.get(word, 0)}
            else:
                tfidf_per_word[word][document_number] = tf * idf_per_word.get(word, 0)


    with open(output_file, 'w') as output_file:
        json.dump(tfidf_per_word, output_file, indent=2)


tf_file = './tf_per_document.json'
idf_file = './idf_per_word.json'
output_file = './tfidf_per_word.json'


calculate_tfidf(tf_file, idf_file, output_file)
