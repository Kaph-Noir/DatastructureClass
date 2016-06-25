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

def print_vertex(list,n):
    print (list[n].n, end=' ')
    print (list.name, end=' ')
    p = a.first
    while p:
        print (a[p.n].name, end = ' ')
        #print (p.n, end = ' ')
        p = p.next
    print('')

def get_user_data():
    f = open('sm_user.txt', 'r')
    i=0
    list=[]
    L=[]
    while True:
        line = f.readline()
        if i % 4 == 0:
            list.append(line.strip())
        i += 1
        if not line: break
    f.close()
    L=[]
    for i in range(len(list)):
        a = list[i]
        a = Vertex()
        a.name = list[i]
        a.n = i
        L.append(a.name)
    print(L)

get_user_data()
