# -----------------------------------------------------------

# Stack Pop

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

    def pop(self):

        if self.height == 0:
            return None

        # temp variable from top to point to
        temp = self.top

        # set top to equal the next down node
        self.top = self.top.next

        # remove node from the stack
        # temp pointer next is pointing to none
        temp.next = None

        self.height -= 1

        # returning the value that we popped
        return temp

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

my_stack.print_stack()

print("")

# removes 11 from the top of the stack
my_stack.pop()
my_stack.print_stack()

# -----------------------------------------------------------




