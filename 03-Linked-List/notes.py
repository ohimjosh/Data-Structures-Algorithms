# -----------------------------------------------------------

# What is the difference b/w a list and linked list?

# linked list do not have indexes
# linked list nodes are spread all over the place
# there is a head, that points to the first node 
# and there is a tail, points to the last node
# each node points to the next to the next to the next etc 
# the last will point to none

# -----------------------------------------------------------

# Linked list Big O

# adding an element to the end of a linked list is O(1)

# removing is more complicated and requires you to iterate 
# through the entire list so it is O(n)
# reason for this is because once you remove the last node
# tail is no longer pointing to anything and so it will need
# to start from the head and iterate throught the list and
# then you can set tail to the last node

# add an element to the front of the linked list is O(1)
# new node will point to the front node
# head will equal to the new node adding it to the linked list

# removing an element from the front of the linked list O(1)
# head will point to the 2nd node 
# this is done by making head equal to head.next

# 11h => 3 => 23 => 7t
# 4 =>
# adding to the middle of the linked list  O(n)
# add it after 23
# start from head and iterate through the list until 23
# we need 4 to point to 7
# set point from 4 equal to pointer pointing from 23 to 7
# 23 will equal to the new node which is 4 
# 11h => 3 => 23 => 4 => 7t

# removing from the middle of the linked list O(n)
# iterate through the list looking for 4 
# we want 23 to point to 7, so set pointer pointing to 23 equal to 
# the point thats pointing to 7 then 4 is removed

# looking up linked list by value or index is O(n)

# -----------------------------------------------------------

# Constructor

# a node is essentially just a dictionary

#{
#    "value": 4,
#    "next": None
#}


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        # create node and pass value onto it
        new_node = Node(value)

        # head points to new node
        self.head = new_node

        # tail points to new node
        self.tail = new_node

        # keep track of length
        self.length = 1

# creating a head, a tail and assigning the node value of 4 
# and length of 1
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
