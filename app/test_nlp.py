from .nlp import (
    get_sentence_scores,
    get_term_frequencies,
    preprocess_text,
    sentence_tokenize,
    summarize_text,
)

input_text = """This is a sample @@text. It is 99used for   testing text processing.
Testing is a good idea and always important part of software development.
Testing ensures that the software is working correctly."""


def test_preprocess_text():
    output_text = preprocess_text(input_text)
    assert output_text == (
        "this is a sample text it is used for testing text processing "
        "testing is a good idea and always important part of software "
        "development testing ensures that the software is working correctly"
    )


def test_get_term_frequencies():
    processed_text = preprocess_text(input_text)
    output_dict = get_term_frequencies(processed_text)
    assert ("testing", 1.0) in output_dict.items()
    assert ("text", 0.6666666666666666) in output_dict.items()
    assert ("processing", 0.3333333333333333) in output_dict.items()


def test_sentence_tokenize():
    output_list = sentence_tokenize(input_text)
    assert output_list[0] == "This is a sample @@text."
    assert output_list[1] == "It is 99used for   testing text processing."


def test_get_sentence_scores():
    processed_text = preprocess_text(input_text)
    term_frequencies = get_term_frequencies(processed_text)
    output_dict = get_sentence_scores(sentence_tokenize(input_text), term_frequencies)
    assert ("This is a sample @@text.", 1.0) in output_dict.items()
    assert (
        "It is 99used for   testing text processing.",
        1.9999999999999998,
    ) in output_dict.items()
    assert (
        "Testing is a good idea and always important part of software development.",
        3.6666666666666665,
    ) in output_dict.items()


def test_summarize_text():
    output_text = summarize_text(text=input_text, n_sentences=2)
    assert output_text == (
        "Testing is a good idea and always important part of software development. "
        "Testing ensures that the software is working correctly."
    )
