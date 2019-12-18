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

########################################################

def hashCode(key,size):
    return key%size


class Item:
    def __int__(self,key,data):
        self.key = key
        self.data = data


def insert_linear_probing(arr,Item):
    size = len(arr)
    idx = hashCode(Item.key)
    while arr[idx]!=None:
        idx +=1
        idx %= size

    arr[idx] = Item

def insert_separate_chaining(arr,Item):
    size = len(arr)
    idx = hashCode(Item.key, size)
    p = arr[idx]

    if p==None:
        p = SinglyLinkedList()
        p.insert_node(Item)
    else:
        p.insert_node(Item)


def search_linear_probing(arr,key):
    size = len(arr)
    idx = hashCode(key, size)
    while arr[idx]==None:
        if arr[idx].key==key:
            return arr[idx]
        else:
            idx += 1
            idx %= size

    return None


def search_separate_chaining(arr,key):
    size = len(arr)
    idx = hashCode(key, size)
    if arr[idx]==None:
        return None
    else:
        p = arr[idx].head
        while p!=None:
            if p.data.key==key:
                return p.data
            else:
                p = p.next
