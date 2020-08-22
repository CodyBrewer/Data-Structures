from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        # Array
        # self.storage = []
        # LinkedList
        self.storage = LinkedList()
    def __len__(self):
        return self.size

    def push(self, value):
        # add an element to the front of our array
        self.size += 1
        # Array
        # self.storage.insert(0, value)
        # LinkedList
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        # Array
        # node = self.storage.pop(0)
        node = self.storage.remove_head()
        return node

new_stack = Stack()
print(len(new_stack))
