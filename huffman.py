'''
File: huffman.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: A program that reads 
    a specified text file, applies the 
    Huffman coding algorithm for decoding 
    using preorder traversal, and outputs 
    the postorder traversal of the decoding 
    tree along with the decoded sequence.
'''
class Tree:
    '''
     A class representing a binary tree node
    '''
    def __init__(self, value):
        '''
        initialises the tree class with value,
        and None for left and right values.

        Parameters: 
            self: object itself
            value: value of node
        '''
        self._value  = value
        self._left = None
        self._right = None

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_value(self):
        return self._value
    
    def set_left(self, value):
        self._left = value

    def set_right(self, value):
        self._right = value

def deconstruct_tree(first, tree, string):
    '''
    This function takes a tree and a string
    as input to decode into a binary string.
    It checks the length of the string and
    performs actions accordingly to create
    the binary string. It is implemented 
    as a recursive function.

    Parameters:
        first: initial tree to be on first called, used by
            function
        tree: tree that need sto be decoded
        string: binary string

    Returns:
        String string
    '''
    if len(string) == 0:
        if tree.get_left() == None and tree.get_right() == None:
            return str(tree.get_value())
        else:
            return ''
        
    elif string[0] == '0':
        if tree.get_left() == None and tree.get_right() == None:
            return str(tree.get_value()) + deconstruct_tree(first, first, string)
        elif tree.get_left() != None:
            return deconstruct_tree(first, tree.get_left(), string[1:])
        else:
            return(first, first, string[1:])

    else:
        if tree.get_left() == None and tree.get_right() == None:
            return str(tree.get_value()) + deconstruct_tree(first, first, string)
        elif tree.get_right() != None:
            return deconstruct_tree(first, tree.get_right(), string[1:])
        else:
            return deconstruct_tree(first, first, string[1:])
        
def reconstruct_tree(tree, preord, inord):
    '''
    This function processes preorder
    and inorder traversals to construct 
    a tree while checking specific conditions
    
    Parameters:
        tree: tree that needs to be created
        preord: preorder traversal list
        inord: inorder traversal list

    Returns:
        tree
    '''
    if len(preord) == 0 or len(inord) == 0:
        return None
    else:
        tree = Tree(preord[0])
        left_inord = inord[0:inord.index(preord[0])]
        right_inord = inord[inord.index(preord[0]) + 1:]

        preord = preord[1:]
        left_preord = preord[0:len(left_inord)]
        right_preord = preord[len(left_inord):]

        tree.set_left(reconstruct_tree(tree.get_left(), left_preord, left_inord))
        tree.set_right(\
            reconstruct_tree(tree.get_right(), right_preord, right_inord))
        return tree
    
def postorder_trav(tree):
    '''
    function to print postorder traversal of the given tree
    using recursion

    Parameters:
        tree: tree object

    returns: 
        String
    '''
    if tree == None:
        return ''
    return postorder_trav(tree.get_left()) + postorder_trav(tree.get_right()) + \
            str(tree.get_value()) + ' '

def main():
    file = open(input('Input file: '))
    preord = file.readline().split()
    inord = file.readline().split()
    tree = reconstruct_tree(None, preord, inord)
    data = file.readline().strip()
    print(postorder_trav(tree))
    print(deconstruct_tree(tree, tree, data).strip())

main()
        
