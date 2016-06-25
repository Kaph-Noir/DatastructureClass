#
# file 호출부
#

f = open('sm_user.txt', 'r')
g = open('sm_friend.txt', 'r')
h = open('sm_word.txt', 'r')

#
# Linked list 구현
#

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
        a.name = v.name
        a.next = self.first
        self.first = a

def print_vertex(vertices, n):
    print(vertices[n].n, end=' ')
    print(vertices[n].name, end=' ')
    p = vertices[n].first
    while p:
        print(vertices[p.n].name, end=' ')
        print (p.n, end = ' ')
        p = p.next
    print('')

#
#
#

def get_friendship_data():
    i=0
    line2list_elem=[]
    L=[]
    while True:
        line = f.readline()
        if i % 4 == 0:
            line2list_elem.append(line.strip())
        i += 1
        #print(init_list)
        if not line: break
    for i in range(len(line2list_elem)):
        a = line2list_elem[i]
        a = Vertex()
        a.name = line2list_elem[i]
        a.n = i
        L.append(a.name)
    #print(len(L))
    #print (L)
    friendship = []
    friend = []
    i = 0
    while True:
        line2 = g.readline()
        #print(line2.strip())
        #friendship.append(line2.strip())
        if i % 3 == 0 :
            friendship.append(line2.strip())

        if not line2: break

        #print(type(friendship))

#line2list_elem 내부 중복 제거
        #friendship = list(set(friendship))

        if i % 3 == 1 :
            friend.append(line2.strip())
        i += 1
    #tmp1 = friendship
    tmp2 = friend


    #print(friendship)
    #print(friend)

    i=0
    LL=[]
    LB=[]
    for i in range(len(friendship)):
        a = Vertex()
        a.n = i
        a.name = friendship[i]
        b = Vertex()
        b.n = i
        b.name = friend[i]
        a.add(b)
        #a.add(tmp2[i])
        print(a.name)
        LL.append(a)
        LB.append(b)
        #print(a.n)
        #print(a.name)
        #print(b.n)
        #print(b.name)
    #print(friendship)
    #print(type(friendship))
    print(LL)
    #print(type(a))
    f.close()
    g.close()
    #return L
'''
    for k in range(len(LB)):
        print(LL[k].name)
        print_vertex(LB, k)
'''
get_friendship_data()




def main():
    return 0