"""This file implements a trigram algorithm that generates a couple of hundred words of text"""


import io
import random
import string


def main(path):
    f = io.open(path, encoding='utf-8')
    book = f.read().replace('\n', ' ').lower()
    new_book = ' '.join(word.strip(string.punctuation) for word in book.split())
    f.close()
    word_list = (new_book.split(' '))
    the_dictionary = {}
    for i in range(len(word_list)-2):
        a_key = "{} {}".format(word_list[i], word_list[i+1])
        a_value = "{}".format(word_list[i+2])
        if a_key in the_dictionary:
            the_dictionary[a_key].append(a_value)
        else:
            the_dictionary[a_key] = [a_value]

    output = []
    start_key = random.choice(list(the_dictionary.keys()))
    value = random.choice(the_dictionary[start_key])
    output = output + start_key.split()
    output.append(value)
    # output_string = ' '.join(output)
    print(output)







main('text.txt')