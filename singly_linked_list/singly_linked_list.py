class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head:Node = None # Stores a node, that corresponds to our first node in the lsit
        self.tail:Node = None# Stores a node, that corresponds to our last node in the lsit
    
    def add_to_head(self, value):
        pass

    def add_to_tail(self, value):
        pass

    def remove_head(self):
        pass

    def contains(self, value):
        pass