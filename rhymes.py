'''
File: word_search.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program reads a file
        that has pronunciations for any
        user input and returns the rhyming 
        words for that user input.
'''
def pronunciation_dictionary(filename):
    '''
    The function reads a file and
    creates a dictionary for different
    pronunciations of a word based 
    on the data provided by the file.
    Parameter: file containing the data
    returns: the dictionary
    '''
    file = open(filename,'r')
    pronunciation_dict = {}
    for line in file:
        section = line.strip().split()
        # checks the word
        word = section[0]
        # checks the pronounciation of the word
        pronunciation = section[1:]
        # creates dictionary with 2-D list as value
        if word in pronunciation_dict:
            pronunciation_dict[word].append(pronunciation)
        else:
            pronunciation_dict[word] = [pronunciation]
    file.close()
    return pronunciation_dict

def rhyming_words(pronunciation_dict, rhyme_the_word):
    '''
    The function uses the dictionary and
    a user input to find the rhyming words
    for the user input. It compares the stress
    and the pre stress of the rhyming words 
    and user input. 
    Parameters: pronunciation dictionary 
                user input
    Returns: rhyming words
    '''
    rhyme_the_word = rhyme_the_word.upper()
    rhyming_words = []
    # iterates over value of user input in dictionary
    for words in pronunciation_dict[rhyme_the_word]:
        stress = ""
        pre_stress = ""
        post_stress = ""
        # iterates over pronounciation of user input
        for letters in range(len(words)):
            if "1" in words[letters]:
                # adds letters to empty strings above
                stress += words[letters]
                pre_stress += words[letters-1]
                post_stress += str(words[letters+1:])
                # iterates over dictionary again
                for key, value in pronunciation_dict.items(): 
                    # iterates over 2d lists
                    for lists in value: 
                        primary_stress = ""
                        primary_phoneme = ""
                        post_primary = ""
                        for word in range(len(lists)):
                            if "1" in lists[word]:
                                # adds word to empty strings 
                                primary_stress += lists[word] 
                                primary_phoneme += lists[word-1]
                                post_primary += str(lists[word +1:])
                        # checks pre stress and primary stress condition
                        if primary_phoneme != pre_stress and stress == primary_stress:
                            if post_stress == post_primary:
                                rhyming_words.append(key)
    return rhyming_words

def print_rhyming_words(rhyming_words):
    '''
    The function sorts the list of
    the rhyming words alphabetically
    and prints them out in a seperate
    line.
    Parameter: list of rhyming words
    Returns: prints the list
    '''
    rhyming_words = sorted(rhyming_words)
    # iterates over the list
    for rhyme in rhyming_words:
        print(rhyme)

def main():
    filename = input()
    rhyme_the_word = input()
    pronounce_dict = pronunciation_dictionary(filename)
    rhymes = rhyming_words(pronounce_dict,rhyme_the_word)
    print_rhyming_words(rhymes)

main()
