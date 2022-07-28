# -----------------------------------------------------------

# Dequeue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node

        else:
            # the last pointer will point to new node
            self.last.next = new_node

            # last node is now the new node
            self.last = new_node

        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        
        else: 
            # first pointer will point to the next node 
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp
        # return temp.value

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()
print("")

# (2) Items - Returns 2 Node
print(my_queue.dequeue())

# (1) Items - Returns 1 Node
print(my_queue.dequeue())

# (0) Items - Returns None
print(my_queue.dequeue())

# -----------------------------------------------------------
