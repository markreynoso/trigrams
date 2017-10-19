"""This file implements a trigram algorithm that generates a couple of hundred words of text"""


import io
import string


def main(path):
    f = io.open(path, encoding='utf-8')
    book = f.read().replace('\n', ' ').lower()
    f.close()
    word_list = (book.split(' '))
    the_dictionary = {}
    for i in range(len(word_list)-2):
        a_key = "{} {}".format(word_list[i], word_list[i+1])
        a_value = "{}".format(word_list[i+2])
        if a_key in the_dictionary:
            the_dictionary[a_key].append(a_value)
        else:
            the_dictionary[a_key] = [a_value]
    print (the_dictionary)







main('text.txt')