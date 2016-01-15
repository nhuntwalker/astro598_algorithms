#linked list
#each node in the list has data and a pointer to the next node
# n1[data, next] -> n2[data, next] -> n3[data, next] ...
# node n1, n2, n3...
# Useful bc you can dynamically increase the size of your
#     data structure without worry

#node n;
class LinkedList(object):
    #we don't delete at tail because we have to traverse
    #the entire list up to the second to last node
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        n = self.head

        if n == None:
            return "This linked list is empty"

        while (n != None):
            print(n.data)
            n = n.next

    def insert_at_head(self, some_data):
        n = Node()
        n.data = some_data
        n.next = self.head

        if self.head == None:            
            self.tail = n

        self.head = n

    def delete_at_head(self):
        if self.head == None:
            raise Exception("List is empty")

        else:
            val = self.head.data
            self.head = self.head.next

            if self.head == None:
                self.tail = None

            return val

    def insert_at_tail(self, some_data):
        n = Node()
        n.data = some_data
        n.next = None

        if self.head == None:
            self.head = n
            self.tail = n

        else:
            self.tail.next = n
            self.tail = n

            if self.head.next == None:
                self.head.next = self.tail


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next




