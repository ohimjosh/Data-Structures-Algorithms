# -----------------------------------------------------------

# Prepend

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

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail 
        pre = self.head

        # while temp is pointing is a node is True
        while(temp.next):
            pre = temp
            temp = temp.next


        # temp is now pointing to None
        # pre is a node before temp and before the tail
        # now we want to set the new tail to pre
        self.tail = pre 
        
        # since it is now tail and the new last node we 
        # want to point it to None
        self.tail.next = None

        self.length -= 1

        # edge case when there is 1 node
        # started at 1 item then we decremented to 0
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            # new node pointer point to the head
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

my_linked_list = LinkedList(2)

my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()


