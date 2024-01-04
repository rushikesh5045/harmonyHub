

import sqlite3

def create_feedback_table():
    connection = sqlite3.connect('feedback.db')
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            document_number INTEGER NOT NULL,
            relevance INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_feedback_table()
