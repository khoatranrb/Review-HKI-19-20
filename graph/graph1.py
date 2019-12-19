class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = [None]*self.V

    def add_edge(self,node1,node2):
        Node1 = Node(node1)
        Node2 = Node(node2)
        Node1.next = self.graph[node2]
        self.graph[node2] = Node1
        Node2.next = self.graph[node1]
        self.graph[node1] = Node2

    def printGraph(self):
        for i in range(self.V):
            print(i,'->',end=' ')
            node = self.graph[i]
            while node!=None:
                print(node.data,'->', end=' ')
                node = node.next
            print('None.')

    def BFS(self, start):
        arr = [False]*self.V
        queue = [start]
        arr[start] = True
        while len(queue)!=0:
            idx = queue.pop(0)
            print(idx,end=' ')
            node = self.graph[idx]
            while node!=None:
                if arr[node.data]==False:
                    queue.append(node.data)
                    arr[node.data]=True
                node = node.next

    def DFS(self,start):
        arr = [False]*self.V
        stack = [start]
        arr[start] = True
        while len(stack)!=0:
            idx = stack.pop()
            print(idx, end=' ')
            node = self.graph[idx]
            while node != None:
                if arr[node.data] == False:
                    stack.append(node.data)
                    arr[node.data] = True
                node = node.next

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        node = self.graph[v]
        list = []
        while node!=None:
            list.append(node.data)
            node = node.next
        for i in list:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def connected_component(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


G = Graph(4)
G.add_edge(0,1)
G.add_edge(2,1)
G.add_edge(2,0)
G.printGraph()
print(G.connected_component())
