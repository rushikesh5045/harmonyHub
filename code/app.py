import json
from flask import Flask, render_template, request, url_for, redirect


import nltk
from nltk.tokenize import word_tokenize
import sqlite3

nltk.download('punkt')  


feedback_db_path = 'feedback.db'
app = Flask(__name__)

word_index_path = './word_index.json'
tf_per_document_path = './tf_per_document.json'
idf_per_word_path = './idf_per_word.json'
tfidf_per_word_path = './tfidf_per_word.json'


with open(word_index_path, 'r') as file:
    word_index = json.load(file)

with open(tf_per_document_path, 'r') as file:
    tf_per_document = json.load(file)

with open(idf_per_word_path, 'r') as file:
    idf_per_word = json.load(file)

with open(tfidf_per_word_path, 'r') as file:
    tfidf_per_word = json.load(file)


stored_document_numbers = {}


new_file_path = './new_file_without_stop_words.json'


def collect_feedback(query, document_number, relevance):
    connection = sqlite3.connect(feedback_db_path)
    cursor = connection.cursor()


    cursor.execute('''
        INSERT INTO feedback (query, document_number, relevance)
        VALUES (?, ?, ?)
    ''', (query, document_number, relevance))

    connection.commit()
    connection.close()


def search_lyrics(query, page=1, results_per_page=10):

    query_words = word_tokenize(query.lower())


    document_scores = {}


    for word in query_words:
        if word in word_index and word in tfidf_per_word:

            word_document_scores = tfidf_per_word[word]


            for document_number, score in word_document_scores.items():
                if document_number not in document_scores:
                    document_scores[document_number] = score
                else:
                    document_scores[document_number] += score


    sorted_results = sorted(document_scores.items(), key=lambda x: x[1], reverse=True)


    start_index = (page - 1) * results_per_page
    end_index = start_index + results_per_page


    paginated_results = [{'document_number': str(doc_number), 'score': score} for doc_number, score in
                         sorted_results[start_index:end_index]]


    stored_document_numbers[query] = [int(result['document_number']) for result in paginated_results]


    feedback_data = []
    for result in paginated_results:
        document_number = int(result['document_number'])
        feedback_value = request.form.get(f'feedback_{document_number}')

        if feedback_value is not None:
            relevance = int(feedback_value)
            collect_feedback(query, document_number, relevance)
            feedback_data.append((document_number, relevance))
    return paginated_results


def get_documents_by_numbers(document_numbers):

    with open(new_file_path, 'r') as file:
        all_documents = json.load(file)


    matching_documents = [doc for doc in all_documents if doc.get('document_number') in document_numbers]

    return matching_documents


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def perform_search():
    query = request.form.get('query') if request.method == 'POST' else request.args.get('query')
    page = request.args.get('page', default=1, type=int)

    if query:
        results = search_lyrics(query, page=page)
        document_numbers = stored_document_numbers.get(query, [])
        matching_documents = get_documents_by_numbers(document_numbers)
        return render_template('results.html', results=results, page=page, matching_documents=matching_documents,
                               query=query)

    return render_template('index.html', error='Please enter a search query.')




@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    query = request.form.get('query')
    document_number = int(request.form.get('document_number'))
    feedback = int(request.form.get('feedback'))


    collect_feedback(query, document_number, feedback)


    return redirect(url_for('perform_search', query=query))



@app.route('/view_feedback')
def view_feedback():
    connection = sqlite3.connect(feedback_db_path)
    cursor = connection.cursor()


    cursor.execute('''
        SELECT * FROM feedback
    ''')

    feedback_data = cursor.fetchall()

    connection.close()

    return render_template('view_feedback.html', feedback_data=feedback_data)


if __name__ == '__main__':
    app.run(debug=True)

