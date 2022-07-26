# -----------------------------------------------------------
# Stacks & Queues

# LIFO
# Last In First Out

# lets say you have a tube container of tennis balls
# you place one in and then a second one
# the only tennis ball that can be taken out is the last one 
# if you have three tennis balls in the tube
# you dont have access to the second one anymore 
# you can only take out the third ball

# lets say we have a list 
# 11 3 23 7
#  0 1  2 3

# if we were to add a item at the end of that list
# Big O: O(1)

# BUT if we were to add an item to the front
# Big O: O(n)
# since we will need to go through the list 

# -----------------------------------------------------------

# Constructor

# creating a single node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        # create first node in the stack
        new_node = Node(value)

        # since we are stacking we only need top
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)

my_stack.print_stack()

# -----------------------------------------------------------
