"""This file tests functions from trigrams file."""

import trigrams

def test_create_list():
    """tests that create_list() returns a list"""
    from trigrams import create_list
    assert type(create_list('text.txt')) == list

def test_create_dictionary_is_dictionary():
    """tests that create_dictionary() returns a dict"""
    from trigrams import create_list
    from trigrams import create_dictionary
    word_list = create_list('text.txt')
    assert type(create_dictionary(word_list)) == dict

def test_create_dictionary_key_has_two_words():
    """tests that the returned dictionary of create_dictionary() has keys with two words"""
    from trigrams import create_list
    from trigrams import create_dictionary
    word_list = create_list('text.txt')
    dictionary = create_dictionary(word_list)
    for key in dictionary:
        assert len(key.split()) == 2

def test_create_dictionary_key_at_least_one_value():
    """tests that the returned dictionary of create_dictionary() has at least one value in each key"""
    from trigrams import create_list
    from trigrams import create_dictionary
    word_list = create_list('text.txt')
    dictionary = create_dictionary(word_list)
    for key in dictionary:
        assert len(dictionary[key]) > 0

# def test_compile_story_is_string():
#     """tests that the returned dictionary of create_dictionary() has at least one value in each key"""
#     from trigrams import main
#     story = main('text.txt', 100)
#     assert type(story) == str

def test_compile_story_contains_correct_number_of_words():
    """tests that the returned dictionary of create_dictionary() has at least one value in each key"""
    from trigrams import main
    story = main('text.txt', 100)
    assert len(story) == 100
 