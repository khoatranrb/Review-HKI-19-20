class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def printLinkedList(head):
    if head:
        print(head.data)
        printLinkedList(head.next)

def insertNodeAtTail(head, data):
    if (head == None):
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head

def insertNodeAtHead(head, data):
    X = head
    y = SinglyLinkedListNode(data)
    y.next = X
    return y

def insertNodeAtPosition(head, data, position):
    i=1
    X = head
    while i!=position:
        X = X.next
        i+=1
    y=X.next
    node = SinglyLinkedListNode(data)
    X.next = node
    node.next = y
    return head

def deleteNode(head, position):
    i=0
    if position ==0:
        return head.next
    X = head
    while i!=position-1:
        X = X.next
        i+=1
    y = X.next.next
    X.next = y
    return head

def reverse(head):
    X = head
    i = 1
    while X.next!=None:
        X = X.next
        i+=1
    res = SinglyLinkedList()
    while i !=0:
        y = head
        for j in range(1,i):
            y = y.next
        res.insert_node(y.data)
        i-=1
    return res.head
