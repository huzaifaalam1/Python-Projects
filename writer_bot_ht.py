'''
File: writer_bot_ht.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: his program uses the Markov 
        Chain Analysis, to generate new
        words in random order after reading
        a textfile and getting input from the user.
        It uses an ADT Hashtable. 
'''

import sys
import random
SEED = 8
NONWORD = "@"

class Hashtable:
    '''
    A class representing a Hashtable.

    It contains the size and key-value pairs
    and has other methods such as put, get and
    hash_key
    .
    '''
    def __init__(self, size):
        '''
        Initializes a Hashtable instance with the given size.

        Args:
            self - object itself
            size - int

        Returns: None
        '''
        self._size = size
        self._pair = [None] * size
    
    def size(self):
        return self._size

    def pair(self):
        return self._pair

    def put(self, key, value):
        '''
        Puts a key-value pair into the hashtable.
        Collisions are resolved with a decrement of -1

        Args:
            key: The key to be inserted.
            value: The value associated with the key

        Returns: None
        '''
        index = self.hash_key(key)
        if self.pair()[index] is None:
            self.pair()[index] = [key, value]
        else:
            index -= 1
            while self.pair()[index] is not None:
                index = (index - 1) % len(self.pair())
            self.pair()[index] = [key, value]

    def get(self, key):
        '''
        Gets the value associated with a key from the hashtable.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if not found.
        '''
        index = self.hash_key(key)
        if self.pair()[index] == None:
            return None
        elif self.pair()[index][0] == key:
            return self.pair()[index][1]
        index = (index - 1) % len(self.pair())
        while self.pair()[index] is not None and index != self.hash_key(key):
            if self.pair()[index][0] == key:
                return self.pair()[index][1]
            index = (index - 1) % len(self.pair())
        return None
    
    def __contains__(self, key):
        '''
        Checks if a key is present in the hashtable.

        Args:
            key: The key to check for.

        Returns:
            bool: True if the key is present, False otherwise
        '''
        if self.get(key) == None:
            return False
        return True

    def hash_key(self, key):
        '''
        Hashes a key.

        Args:
            key: The key to be hashed.

        Returns:
            hashed key
        '''
        hash_value = 0
        for char in key:
            hash_value = 31*hash_value + ord(char)
        return hash_value % self._size

    def __str__(self):
        return str(self._pair)

def sentence_list(list_hash, dict_hash, num_of_words):
    '''
    Generates a sentence based on a list of words and a dictionary.

    Args:
        list_hash: A list of words.
        dict_hash: A hashtable containing word mappings.
        num_of_words: The number of words to generate.

    Returns:
        str: The generated sentence
    '''
    i = 0
    list_of_words = []
    sentence_data = ""
    str = ""
    while len(list_of_words) != num_of_words:
        key = " ".join(list_hash)
        value = dict_hash.get(key)
        if len(value) > 1:
            list_of_words.append(value[random.randint(0, len(value) - 1)])
        elif len(value) == 1:
            list_of_words.append(value[0])

        list_hash.append(list_of_words[i])
        list_hash = list_hash[1:]
        i += 1

    while len(list_of_words) > 10:
        str = " ".join(list_of_words[0:10])
        sentence_data += str + "\n"
        str = ""
        list_of_words = list_of_words[10:]
    
    sentence_data += " ".join(list_of_words)
    return sentence_data

def add_hash(words, dict_hash, list_hash):
    '''
    Matches hash_list to key/value pairs.

    Args:
        words: A list of words.
        dict_hash: A hashtable for word mappings.
        list_hash: list used to insert strings to table
    
    Returns: None
    '''
    for element in range(len(words)):
        key = " ".join(list_hash)
        if key in dict_hash:
            dict_hash.get(key).append(words[element])
        else:
            dict_hash.put(key, [words[element]])
        list_hash.append(words[element])
        list_hash = list_hash[1:]

def main():
    random.seed(SEED)

    file = open(input(), "r")
    M = int(input())
    n = int(input())
    num_of_words = int(input())

    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_of_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    words = []
    for line in file:
        line = line.split()
        words += line

    dict_hash = Hashtable(M)
    list_hash = [NONWORD] * n
    add_hash(words, dict_hash, list_hash)

    list_hash = [NONWORD] * n
    list_made = sentence_list(list_hash, dict_hash, num_of_words)

    print(list_made)

main()