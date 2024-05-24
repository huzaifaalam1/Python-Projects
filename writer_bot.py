'''
File: writer_bot.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program uses the Markov 
        Chain Analysis, to generate new
        words in random order after reading
        a textfile and getting input from the user
        for the prefix and length of word.
'''
import random

SEED = 8
NONWORD = ''

def make_tuple(word, num):
    '''
    creates a tuple of word, n times

    Parameters:
        word: tuple to be created of word
        n: number of times to be repeted

    Returns:
        tup: tuple 
    '''
    tup = []
    for i in range(num):
        tup.append(word)
    return tuple(tup)

def move_tuple(tup, value):
    '''
    Parameters:
        tup: tuple
        value: shift by value

    Returns:
        t: tuple
    '''
    t = tup[1:]
    t = t + (value,)
    return t

def make_prefix(text, prefix):
    '''
    Create a prefix tuple from the given text

    Parameter:
        text: data from file  
        prefix: length

    Returns: 
        temporary: tuple
    '''
    temporary = []
    for items in text[:prefix]:
        temporary.append(items)
    temporary = tuple(temporary)
    return temporary

def read_file(file_name):
    '''
    Read and process a file to extract words.

    Args:
        file_name: name of file to read.

    Returns:
        list: list of words 
    '''
    data = []
    file = open(file_name)
    for items in file:
        items = items.strip().split()
        data += items
    return data

def create_dictionary(data, prefix):
    '''
    Create a dictionary based on input data

    Args:
        data: data from file
        prefix: The prefix length for dictionary creation.

    Returns:
        dict: A dictionary with the words
    '''
    word_dict = {}
    # Create a tuple key using make_tuple function
    key = make_tuple(NONWORD, prefix)
    for word in range(len(data)):
        if key in word_dict:
            word_dict[key].append(data[word])
        else:
            word_dict[key] = [data[word]]
        key = move_tuple(key, data[word])
    return word_dict

def format_print(file_data, n, num_words, dic):
    '''
    The code randomly orders words into a list,
    forms prefixes from user input, selects
    random prefixes from the dictionary, 
    transitions to new tuples, and prints the
    output in 10-word lines until reaching
    the specified word count.

    Parameter:
        file_data: data from file
        n: prefix shift
        num_words: number of words
        dic: dictionary
    '''
    word = ''
    words = []
    counter = num_words
    # Iterate through the first n items in file_data
    for items in file_data[:n]:
        words.append(items)
    # Create a prefix using make_prefix function
    prefix = make_prefix(file_data, n)
    
    for text in range(num_words+1):
        if prefix in dic:
            if len(dic[prefix]) > 1:
                word = dic[prefix][random.randint(0, len(dic[prefix]) - 1)]
            else:
                word = dic[prefix][0]
        words.append(word)
        prefix = move_tuple(prefix, word)

    for i in range(0, num_words, 10):
        if counter >= 10:
            print(' '.join(words[i: i + 10]))
        else:
            print(' '.join(words[i: i + counter]))
        counter -= 10

def main():
    random.seed(SEED)
    file = input()
    n = int(input())
    num_words = int(input())

    file_data = read_file(file)
    dict = create_dictionary(file_data, n)

    format_print(file_data, n, num_words, dict)

main()