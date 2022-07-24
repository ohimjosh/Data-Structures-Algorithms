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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # pass value to append
        # self is a parameter so we know it is a method
        # instead of a function
        new_node = Node(value)

        # check if list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            # last node of list will be new node
            self.tail.next = new_node

            # tail will point to new node
            self.tail = new_node

        # increase length by 1 since we appened a new node
        self.length += 1
        return True
            

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()
