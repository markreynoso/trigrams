"""This file tests functions from trigrams file."""

import trigrams

def test_main():
    from trigrams import main
    assert main('text.txt', num_words) == list