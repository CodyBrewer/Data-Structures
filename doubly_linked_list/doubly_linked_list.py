"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        # check if there is a previous and next node for the node
        # there is a previous node
        if self.prev:
            # set the previous node of the node we are deleting (self) next node to the next node in the list
            self.prev.next = self.next
        # there is a next node
        if self.next:
            # set the next node's previous node the the previous node of the node we are deleting(self)
            self.next.prev = self.prev
        # our self next and prev property are no longer pointing to any node so I am garbage collected by the pygc        
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new_node using value
        new_node = ListNode(value)
        # check if there are nodes in the linked_list
        # if there are no nodes
        if self.head is None and self.tail is None:
            # set head_node in list to the new_node
            self.head = new_node
            # set tail_node in list to the new_node
            self.tail = new_node
        # there are nodes in the linked_list
        else:
            # set next property on the new_node to current head_node
            new_node.next = self.head
            # set previous property on the current head_node to the new_node
            self.head.prev = new_node
            # set the head to the new_node
            self.head = new_node
        # increment length of the list by 1
        self.length += 1 
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check if there is a head
        # there is no head
        if self.head is None:
            # there is no head to remove so do nothing
            return None
        # there is a head
        # store the head value so we can return it after we delete it
        head_value = self.head
        # delete the head node
        self.delete(self.head)
        # return the head_value
        return head_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create the new node with the passed in value
        new_node = ListNode(value)
        # check if there are nodes in the list
        # if there are no nodes
        if self.head is None and self.tail is None:
            # set the head to the new node
            self.head = new_node
            # set the tail to the new_node
            self.tail = new_node
        # there are nodes in the list
        else:
            # set the tail node next value to the new node
            self.tail.next = new_node
            # set the tail to the new_node previous node
            new_node.prev = self.tail
            # set the tail to the new node
            self.tail = new_node
        # incrment the list length by 1
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # check if there is a tail
        # there is no tail
        if self.tail is None:
            # nothing to remove so do nothing
            return None
        # there is a tail value
        # store the tail value to return later
        tail_value = self.tail
        # delete the tail node
        self.delete(self.head)
        # return the delete value
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if there are nodes in the list
        if self.head is None and self.tail is None:
            # there are no nodes so nothing to remove
            return None
        # if there is only one node
        if node is self.head and node is self.tail:
            # delete the node
            node.delete()
        # there are at least two nodes in the list
        # the node is the head_node
        if node is self.head:
            # set the next node as the head of the list
            self.head = node.next
            # delete the passed in node
            node.delete()
        # the node is the tail_node
        if node is self.tail:
            # set the tail node the tail_node previous node
            self.tail = node.prev
            # delete the node
            node.delete()
        # the node is just a node in the list
        else:
            # delete the node
            node.delete()
        # decrement length by 1
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass