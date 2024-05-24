class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        '''
        Sorts the linked list in non-decreasing order using insertion sort.

        Returns:
                A sorted list
        '''
        sort_head = None 
        while self._head:
            # Remove an element from the original list
            curr_element = self.remove()
            # If sorted list is empty or the current element is greater than or equal to the head of the sorted list
            if sort_head == None or sort_head._value <= curr_element._value:
                curr_element._next = sort_head
                sort_head = curr_element
            else: 
                # If the current element is smaller than the head of the sorted list,
                # find the correct position to insert the current element in the sorted list
                current = sort_head
                while current._next and current._next._value > curr_element._value: 
                    current = current._next
                # Insert the current element in the sorted list
                curr_element._next = current._next
                current._next = curr_element

        self._head = sort_head
    
    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next

def main():
    filename = input()
    file = open(filename,'r')
    linked_list = LinkedList()
    for line in file:
        nums = line.strip().split()
        if len(nums) != 0:
            for num in nums:
                linked_list.add(Node(int(num)))
    linked_list.sort()
    print(linked_list)
    file.close()

main()