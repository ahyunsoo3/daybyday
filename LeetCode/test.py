# Node class
class Node:

    # Function to initialize the 
    # node object
    def __init__(self, data):
        # Assign data
        self.data = data

        # Initialize next as null
        self.next = None

    # Linked List class


class LinkedList:

    # Function to initialize the 
    # Linked List object
    def __init__(self):
        self.head = None


# This function is in LinkedList class
# Function to insert a new node at
# the beginning
def push(self, new_data):
    # 1 & 2: Allocate the Node &
    #        Put in the data
    new_node = Node(new_data)

    # 3. Make next of new Node as head
    new_node.next = self.head

    # 4. Move the head to point to new Node
    self.head = new_node


# Ref : https://www.geeksforgeeks.org/python-program-for-inserting-a-node-in-a-linked-list/