class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

def insert(tree, data):
    if tree.root==None:
        tree.root = Node(data)
    else:
        root = tree.root
        while True:
            if root.info>data:
                if root.left==None:
                    root.left=Node(data)
                    break
                else:
                    root = root.left
            elif root.info==data:
                break
            else:
                if root.right==None:
                    root.right=Node(data)
                    break
                else:
                    root = root.right


def height(root):
    if root == None:
        return 0
    else:
        return 1+max(height(root.left), height(root.right))


def inOrder(root):
    if root==None:
        return None
    inOrder(root.left)
    print(root.info, end=' ')
    inOrder(root.right)

def preOrder(root):
    if root==None:
        return None
    print(root.info, end=' ')
    inOrder(root.left)
    inOrder(root.right)

def postOrder(root):
    if root==None:
        return None
    inOrder(root.left)
    inOrder(root.right)
    print(root.info, end=' ')

def levelOrder(arr):
    if len(arr)==0:
        return None
    elif arr[0]==None:
        return None
    else:
        print(arr[0].info, end=' ')
        if arr[0].left!=None:
            arr.append(arr[0].left)
        if arr[0].right!=None:
            arr.append(arr[0].right)
        arr = arr[1:]
        levelOrder(arr)


def find_way(root,data):
    arr = []
    while root.info!=data:
        arr.append(root.info)
        if root.info>data:
            root = root.left
        else:
            root = root.right
    return arr

def lowest_common_ancestor(root,data1,data2):
    arr1 = find_way(root,data1)
    arr2 = find_way(root,data2)
    i=0
    print(arr1)
    print(arr2)
    while True:
        if arr1[i]!=arr2[i]:
            return arr1[i-1]
        else:
            i+=1
            if i>=len(arr1) or i>=len(arr2):
                return arr1[i-1]


def rotate_left(root):
    x = root.right
    T2 = x.left
    root.right = T2
    x.left = root
    return x

def rotate_right(root):
    x = root.left
    T2 = x.right
    root.left = T2
    x.right = root
    return x

def get_balance(root):
    return height(root.left)-height(root.right)

def insert_avl(tree,data):
    insert(tree,data)
    if get_balance(tree.root)>1 and data<tree.root.left.info:
        tree.root = rotate_right(tree.root)
    elif get_balance(tree.root)<-1 and data>tree.root.right.info:
        tree.root = rotate_left(tree.root)
    elif get_balance(tree.root)>1 and data>tree.root.left.info:
        tree.root.left = rotate_left(tree.root.left)
        tree.root = rotate_right(tree.root)
    elif get_balance(tree.root)<-1 and data<tree.root.right.info:
        tree.root.right = rotate_right(tree.root.right)
        tree.root = rotate_left(tree.root)
