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

