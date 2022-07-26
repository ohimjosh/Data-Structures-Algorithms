#-----------------------------------------------------------

# Stack Push

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node

        else:
            # next new node will point to the new node on top
            new_node.next = self.top

            # top node is now new node
            self.top = new_node

        self.height += 1
        return True

my_stack = Stack(2)
my_stack.push(1)

my_stack.print_stack()

# -----------------------------------------------------------
