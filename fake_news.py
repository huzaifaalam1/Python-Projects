'''
File: fake_news.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program reads a file
        and checks for titles and topics. 
'''

import csv
import string

class Node:
    '''
    An object of the Node class represents 
    information about a word given from a
    title. 
    '''
    def __init__(self, word):
        '''
        Initializes a Node object with a given word and sets the count to 1.

        Parameters:
            word: A string representing the word for the Node.
        '''
        self._word = word
        self._count = 1
        self._next = None

    def word(self):
        '''
        Gets the word stored in the Node.

        Returns:
            A string representing the word.
        '''
        return self._word

    def count(self):
        '''
        Gets the count of occurrences for the word in the Node.

        Returns:
            An integer representing the count.
        '''
        return self._count

    def next(self):
        '''
        Returns the next Node in the linked list.

        Returns:
            A Node object representing the next node
        '''
        return self._next

    def set_next(self, target):
        '''
        Sets the next Node in the linked list.

        Args:
            target: A Node object representing the next node to be set
        '''
        self._next = target
    
    def incr(self):
        '''
        Increases the count of occurrences for the word in the Node by 1.
        '''
        self._count += 1
    
    def __str__(self):
        '''
        A string representation of the Node.

        Returns:
            A formatted string containing the word and its count.
        '''
        return "{} : {}".format(self._word, self._count)

class LinkedList:
    '''
    An object of the LinkedList class represents information about title,
    and implements nodes.
    '''
    def __init__(self):
        '''
        Initializes an empty LinkedList object 
        with a head node set to None.
        '''
        self._head = None

    def is_empty(self):
        '''
        Checks if the LinkedList is empty.

        Returns:
            True if the LinkedList is empty, False otherwise.
        '''
        return self._head == None

    def head(self):
        '''
        Gets the head node of the LinkedList.

        Returns:
            A Node object representing the head node.
        '''
        return self._head

    def update_count(self, word):
        '''
        Updates the count of occurrences for a given word in the LinkedList.

        Args:
            word: A string representing the word to update the count for.
        '''
        if self.search(word) == True:
            current = self._head
            while current != None:
                if current._word == word:
                    current.incr()
                current = current._next 
        else:
            new_word = Node(word)
            self.add(new_word)

    def search(self, present):
        '''
        Searches for a given word in the LinkedList.

        Args:
            present: A string representing the word to search for.

        Returns:
            True if the word is found in the LinkedList, False otherwise.
        '''
        current = self._head
        while current != None:
            if current._word == present:
                return True
            current = current._next
        return False

    def rm_from_hd(self):
        '''
        Removes and returns the head node of the LinkedList.

        Returns:
            The removed head node.
        '''
        assert self._head is not None
        node = self._head
        self._head = node._next
        node._next = None
        return node

    def insert_after(self, node1, node2):
        '''
        Inserts a new node (node2) after a specified node (node1) in the LinkedList.

        Args:
            node1: A Node object representing the node 
            after which to insert node2.
            node2: A Node object representing the node
            to be inserted.
        '''
        assert node1 is not None
        node2._next = node1._next
        node1._next = node2

    def sort(self):
        '''
        Sorts the LinkedList based on word counts.

        Returns:
            A sorted LinkedList object
        '''
        sorted = LinkedList()
        if self.head() != None:
            sorted.add(self.rm_from_hd())
        while not self.is_empty():
            sort_this = self.rm_from_hd()
            current = sorted.head()
            if current.count() < sort_this.count():
                sorted.add(sort_this)
            else:
                while current != None:
                    if current.next() == None or current.next().count()\
                        < sort_this.count():
                        sorted.insert_after(current, sort_this)
                        break
                    current = current.next()
        self._head = sorted.head()
        return self
    
    def add(self, node):
        '''
        Adds a new node to the beginning of the LinkedList.

        Args:
            node: A Node object representing the node to be added.
        '''
        node._next = self._head
        self._head = node
        

    def get_nth_highest_count(self, n):
        '''
        Retrieves the nth highest count node in the LinkedList.

        Args:
            n: An integer representing the nth highest count to retrieve.

        Returns:
            The Node object with the nth highest count.
        '''
        n = int(n)
        pos = 0
        initial = self.head()
        curr = initial
        while curr != None:
            if pos == n:
                return curr

            pos += 1
            prev = curr
            next = prev.next()
            curr = next

    def print_upto_count(self, n):
        '''
        Prints nodes in the LinkedList up to a specified count.

        Args:
            n: An integer representing the count threshold.
        '''
        current = self._head
        while current:
            if current.count() >= n:
                print("{} : {:d}".format(current.word(), current.count()))
            current = current.next()
    
    def __str__(self):
        '''
        A string representation of the LinkedList.

        Returns:
            A string representation of the LinkedList,
            showing its nodes and counts.
        '''
        string = "Head ->"
        current = self.head()

        while True:
            if current is None:
                string += "None"
                break
            string += str(current) + " ->"
            current = current.next()

        return string


def read_file(filename, linked_list):
    '''
    Reads a CSV file, extracts words from specific 
    columns, and updates the word counts in a linked list.

    Args:
        filename: A string representing the 
        path to the CSV file.

        linked_list: An instance of LinkedList 
        where word counts will be updated.

    Returns:
        word_count: A list containing the extracted words
        from the CSV file.
    '''
    file = open(filename, 'r')
    csvreader = csv.reader(file)
    word_count = []

    for line in csvreader:
        if line[0][0] != '#':
            # Extract words from the 5th column and convert to lowercase
            words = line[4].lower().split()
            for i in words:
                word = ''
                for letter in i:
                    if letter in string.punctuation or letter in string.whitespace:
                        if len(word) <= 2:
                            word = ''
                        if len(word) > 2:
                            word_count.append(word)
                            word = ''
                    else:
                        word += letter
            
                if len(word) > 2:    
                    word_count.append(word)

    for count in word_count:
        linked_list.update_count(count)
            
    file.close()
    return word_count

def main():
    file = input()
    n = input()
    linked_list = LinkedList()

    read_file(file, linked_list)
    linked_list.sort()

    value = linked_list.get_nth_highest_count(n)
    linked_list.print_upto_count(value.count())

main()