def sum_node(level):
    return 2**level - 1

def get_level(node):
    i=1
    while 2**i-1<node:
        i+=1
    return i

def get_possion(node):
    level = get_level(node)
    arr_pos = [0]*(2**(level-1))
    idx = node - sum_node(level-1)
    arr_pos[idx-1] = 1
    return arr_pos

def get_way(arr_pos):
    arr = arr_pos
    list = []
    while len(arr)>1:
        l = len(arr)//2
        if sum(arr[:l])>sum(arr[l:]):
            list.append(0)
            arr = arr[:l]
        else:
            list.append(1)
            arr = arr[l:]
    return list

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class Max_heap:
    def __init__(self):
        self.root = None

    def insert(self,arr):
        length = len(arr)
        for i in range(length):
            j = i+1
            if self.root==None:
                self.root = Node(arr[i])
            else:
                arr_pos = get_possion(j)
                arr_way = get_way(arr_pos)
                len_way = len(arr_way)

                way = [self.root.info]
                root = self.root
                for k in range(len_way-1):
                    if arr_way[len_way-k-1]==0:
                        root = root.left
                        way.append(root.info)
                    else:
                        root = root.right
                        way.append(root.info)
                way.append(arr[i])
                way.sort()

                self.root.info = way.pop()
                root = self.root
                for k in range(len_way-1):
                    if arr_way[len_way-k-1]==0:
                        root.left.info = way.pop()
                        root = root.left
                    else:
                        root.right.info = way.pop()
                        root = root.right

                if arr_way[0]==1:
                    root.right = Node(way[0])
                else:
                    root.left = Node(way[0])

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

tree = Max_heap()
tree.insert([0,1,7,8])
levelOrder([tree.root])

