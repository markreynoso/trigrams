"""This file implements a trigram algorithm that generates a couple of hundred words of text"""


import io
import random
import string


def main(path, num_words): # pragma: no cover
    create_the_list = create_list(path)
    dictionary = create_dictionary(create_the_list)
    new_story = compile_story(dictionary, num_words)



def create_list(path):
    """This function copies a text file and turns it into a list."""
    f = io.open(path, encoding='utf-8')
    book = f.read().replace('\n', ' ').lower()
    new_book = ' '.join(word.strip(string.punctuation) for word in book.split())
    f.close()
    word_list = (new_book.split(' '))
    return word_list


def create_dictionary(word_list):
    """This function takes a list and creates a dictionary."""
    the_dictionary = {}
    for i in range(len(word_list)-2):
        a_key = "{} {}".format(word_list[i], word_list[i+1])
        a_value = "{}".format(word_list[i+2])
        if a_key in the_dictionary:
            the_dictionary[a_key].append(a_value)
        else:
            the_dictionary[a_key] = [a_value]
    return the_dictionary


def compile_story(the_dictionary, num_words):
    """This function takes a dictionary and creates a story from randomly selecting words."""
    start_key = random.choice(list(the_dictionary.keys()))
    output = start_key.split()
    while len(output) < num_words:
        search_string = output[-2] + " " + output[-1]
        value = random.choice(the_dictionary[search_string])
        output.append(value)
    output = ' '.join(output)
    print (output)
    return output





main('large_txt.txt', 500)