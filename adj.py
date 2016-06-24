class Adj:
    def __init__(self):
        self.n = 0
        self.next = None

class Vertex:
    def __init__(self):
        self.n = 0
        self.first = None
    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

f = open('sm_friend.txt')

for line in f:
    if line.strip():
        line = line[0:-1]

def main():
    node.add(node)