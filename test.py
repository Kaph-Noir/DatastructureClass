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
    print (list[n].name, end=' ')
    p = list[n].first
    while p:
        print (list[p.n].name, end = ' ')
        print (p.n, end = ' ')
        p = p.next
    print('')

def get_user_data():
    f = open('sm_user.txt', 'r')
    i=0
    list=[]
    while True:
        line = f.readline()
        if i % 4 == 0:
            list.append(line.strip())
        i += 1
        if not line: break
    f.close()
    for i in range(len(list)):
        list[i] = Vertex()
        list[i].n = i
        list[i].name = list[i]

    for j in range(0, 8):
        print_vertex(list, j)
    #print (list)

get_user_data()