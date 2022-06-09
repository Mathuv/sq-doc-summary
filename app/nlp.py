import re
import nltk
from heapq import nlargest


def preprocess_text(text: str) -> str:
    """
    Preprocess the text.

    Steps:
    1. remove the punctuations and numbers
    2. remove extra spaces
    3. lowercase the text

    """
    if text:
        # Remove the punctuations and numbers
        text = re.sub(r"[^a-zA-Z]", " ", text)
        # Remoce extra spaces
        text = re.sub(r"\s+", " ", text).strip()
        # convert to lowercase
        text = text.lower()

    return text


def sentence_tokenize(text: str) -> list[str]:
    """
    Tokenize the text into sentences.

    """
    return nltk.sent_tokenize(text) if text else []


def word_tokenize(text: str) -> list:
    """
    Tokenize the text into words.

    """
    return nltk.word_tokenize(text) if text else []


# def remove_stopwords(text: str) -> str:
#     stopwords = nltk.corpus.stopwords.words("english")
#     return [word for word in text if word not in stopwords] if text else text


def get_term_frequencies(text: str) -> dict[str, float]:
    """Find weighted frequencies of words in the text."""
    stopwords = nltk.corpus.stopwords.words("english")
    term_frequencies = {}

    # calculate the word frequencieskk
    for term in nltk.word_tokenize(text):
        if term not in stopwords:
            if term in term_frequencies:
                term_frequencies[term] += 1
            else:
                term_frequencies[term] = 1

    # calculate the weighted frequencies
    maximum_frequncy = max(term_frequencies.values())
    for term in term_frequencies:
        term_frequencies[term] = term_frequencies[term] / maximum_frequncy

    return term_frequencies


def get_sentence_scores(
    sentence_list: list[str], term_frequencies: dict[str, float]
) -> dict[str, float]:
    """
    Get the sentence scores.
    """
    sentence_scores = {}
    for sent in sentence_list:
        for term in nltk.word_tokenize(sent.lower()):
            if term in term_frequencies and len(sent.split(" ")) < 30:
                if sent in sentence_scores:
                    sentence_scores[sent] += term_frequencies[term]
                else:
                    sentence_scores[sent] = term_frequencies[term]

    return sentence_scores


def summarize_text(text: str, n: int = 5) -> str:
    """
    Summarize the text.

    Steps:
    1. preprocess the text
    2. tokenize the text(convert text to sentences)
    3. find the term frequencies
    4. calculate the sentence scores
    5. find the top n sentences
    6. return the summary text

    """
    # Find the term frequencies
    preprocessed_text: str = preprocess_text(text)
    term_frequencies = get_term_frequencies(preprocessed_text)

    # Calculate the sentence scores
    sentences: list[str] = sentence_tokenize(text)
    sentence_scores = get_sentence_scores(sentences, term_frequencies)

    summary_sentences = nlargest(n, sentence_scores, key=lambda k: sentence_scores[k])

    return " ".join(summary_sentences)
