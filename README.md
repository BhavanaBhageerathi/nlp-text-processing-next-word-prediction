# NLP Text Processing and Next Word Prediction

## Overview

This project demonstrates fundamental Natural Language Processing (NLP) techniques using Python libraries NLTK and spaCy.

It explores text preprocessing techniques such as tokenization, stopword removal, stemming, lemmatization, and Part-of-Speech (POS) tagging.

Additionally, it implements a simple next-word prediction mechanism using a Bigram language model.

## Features

### Text Processing

* **Tokenization:** Splits text into individual words and sentences.
* **Stopword Removal:** Removes commonly occurring words that contribute less meaning to the text.
* **Stemming:** Reduces words to their root forms using Porter Stemmer.
* **Lemmatization:** Converts words into their dictionary forms using WordNet Lemmatizer.
* **POS Tagging:** Identifies parts of speech using spaCy.

### Next Word Prediction

* Generates Bigrams from tokenized text.
* Creates a dictionary mapping words to their possible subsequent words.
* Predicts the next word by randomly selecting from the available Bigram possibilities.

## Technologies Used

* Python
* NLTK
* spaCy
* Collections
* Random

## Libraries and Resources

* NLTK: Tokenization, stopword removal, stemming, lemmatization, and Bigram generation.
* spaCy: Part-of-Speech tagging.
* WordNet: Dictionary resource used for lemmatization.
* en_core_web_sm: spaCy English language model.

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/your-username/nlp-text-processing-next-word-prediction.git
```

### 2. Navigate to the project folder

```bash
cd nlp-text-processing-next-word-prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 7. Run the project

```bash
python nlp_text_processing.py
```

The required NLTK resources (punkt, punkt_tab, stopwords, and wordnet) are downloaded by the program when executed.

## Sample Text

The project uses the following sample text:

"The cat sat on the mat. The dog lay on the rug. The cat chased the dog. The dog barked at the cat."

The NLP techniques are applied to this text to demonstrate different text processing operations.

## Next Word Prediction

The project uses a Bigram model, where each word is associated with the word that follows it in the sample text.

For example, given the word "the", the program randomly selects one of its possible following words.

**Note:** This is a basic statistical prediction approach, not a trained neural language model.

## Author

Bhavana Bhageerathi
