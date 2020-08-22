class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head:Node = None # Stores a node, that corresponds to our first node in the lsit
        self.tail:Node = None# Stores a node, that corresponds to our last node in the lsit

    def __str__(self):
        output = ''
        current_node = self.head # create a tracker node variable
        while current_node is not None: # loop untils its NONE
            output += f'{current_node.value} -> '
            current_node = current_node.next_node # update the tracker node to the next node
        return output

    def add_to_head(self, value):
        # Create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new__node should point to current head
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        # Create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if lsit only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elementts in the lsit
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    
    def remove_tail(self):
        # if list is empty do nothing
        if not self.head:
            return None
        if self.head.next_node is None:
            tail_value = self.tail.value
            self.tail = None
            self.head = None
            return tail_value
        current = self.head
        tail_value = self.tail.value
        while current.next_node != self.tail:
            current = current.next_node
        current.next_node = None
        self.tail = current
        return tail_value
    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the ndoe we are look for 
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False