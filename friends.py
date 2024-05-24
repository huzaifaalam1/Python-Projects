'''
File: friends.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program reads a file and uses
        the classes from linked_list.py to store
        friends and print them in regards to common friends.
'''

from linked_list import *

def add_friend(lines):
    '''
    Create a friend list based on input lines.

    Args:
        lines: List of input lines containing friend pairs.

    Returns:
        LinkedList: A linked list representing the friend connections.
    '''
    friend_list = LinkedList()

    for line in lines:
        line = line.split(" ")
        names = []
        for name in line:
            if name != "":
                names.append(name)
            sorted(names)

        if len(names) != 0:
            friend1 = Node(names[0])
            friend2 = Node(names[1])

            friend_list.add(friend1)
            friend_list.add(friend2)

            friend_list.add_friend(friend1, friend2)
            friend_list.add_friend(friend2, friend1)

    friend_list.sort()
    return friend_list

def common_friends(friends_list):
    '''
    Find common friends between two given names in a friend list.

    Args:
        friends_list: The linked list representing the friend connections.

    Returns:
        Prints the common friends between the given names.
    '''
    name_1 = input("Name 1: ")
    name_2 = input("Name 2: ")
    flag = True
    # Checks if name_1 is in the friend list
    if friends_list.checks(name_1) == False:
        flag = False
        print("ERROR: Unknown person "  + name_1)
    # Checks if name_2 is in the friend list
    elif friends_list.checks(name_2) == False:
        flag = False
        print("ERROR: Unknown person "  + name_2)

    if flag:
        # Find common friends between name_1 and name_2
        friend_list = friends_list.common_friends(name_1, name_2)
        
        if len(friend_list) == 0:
            print('')
        else:
            print("Friends in common:")
            for friend in friend_list:
                print(friend)

def main():
    filename = input("Input file: ")
    file = open(filename,"r")
    data = file.read().split("\n")
    friends_list = add_friend(data)
    common_friends(friends_list)
    file.close()
main()