

# Lyrics Finder

A music lyrics search engine that allows users to search for song lyrics, filter results, and explore detailed information about artists and songs.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Features](#features)
- [Preprocessing](#preprocessing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

Welcome to our Music Lyrics Search Engine! This project aims to provide users with a seamless experience for searching and exploring song lyrics. Whether you're looking for the lyrics to your favorite song or exploring new artists, our search engine has got you covered.

## Getting Started

To get started with the Music Lyrics Search Engine, follow the steps below.
- Download and extract the zip file.
- Go the Code folder.
- Open VsCode in that folder.

### Prerequisites

Make sure you have the following installed:

- Python 3
- Flask
- Nltk



## Usage
1. Run the `python database_setup.py`(If you are using MacOS use  `python3 database_setup.py`)
2. Run the application using `python app.py`(If you are using MacOS use  `python3 app.py`).
3. Open your browser and go to [http://127.0.0.1:5000/](http://localhost:5000) link visible in your terminal.
4. Enter your search query and explore the results.
## Preprocessing

The lyrics data undergoes preprocessing to enhance the search experience. Preprocessing steps include:

- **Tokenization:** Breaking down the lyrics into individual words for efficient search.
- **Lowercasing:** Converting all text to lowercase to ensure case-insensitive searches.
- **Stop Word Removal:** Eliminating common words that do not contribute much to the meaning.
- **TF-IDF Calculation:** Computing TF-IDF scores to quantify the importance of words in each document.

## Features

- **Lyrics Search:** Quickly find song lyrics by searching for the song title, artist, or keywords.
- **Filtering Options:** Refine your search results by applying filters, such as artist name or document number.
- **Detailed Information:** Explore detailed information about each result, including the artist's name, song title, and full lyrics.
- **Feedback Functionality:**
Our search application includes a feedback functionality that allows users to provide relevance feedback on the displayed search results. This feedback helps improve the accuracy and effectiveness of future searches.

## How It Works

1. **Filtering Search Results:** Users can apply filters to refine their search results based on criteria such as artist, song, and document number.

2. **Viewing Search Results:** The application displays matching documents according to the applied filters. Each document includes information such as the document number, artist name, song name, and lyrics.

3. **Relevance Feedback Form:** For each displayed document, there is a "Feedback Section" containing a form where users can provide relevance feedback. The feedback is a numerical value from 1 to 5, representing how relevant the document is to their query.

4. **Submitting Feedback:** Users submit their feedback using the form. This information is then processed to enhance the relevance of search results in future queries.

5. **Feedback Visibility:** Once feedback is submitted, the feedback section for that specific document and query combination is disabled. This prevents users from providing multiple feedback entries for the same document and query.



## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- Special thanks to *Musixmatch* for providing the song lyrics API.

## Link for Documents
- https://drive.google.com/file/d/1RXk5wSHoYQZm8mn7XHDHQ18E2uZ8lJQJ/view?usp=sharing


