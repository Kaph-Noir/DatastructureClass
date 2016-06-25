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
        a.next = self.first
        self.first = a

def get_friendship_data():
    i=0
    init_list=[]
    L=[]
    while True:
        line = f.readline()
        if i % 4 == 0:
            init_list.append(line.strip())
        i += 1
        #print(init_list)
        if not line: break
    for i in range(len(init_list)):
        a = init_list[i]
        a = Vertex()
        a.name = init_list[i]
        a.n = i
        L.append(a.name)
    #print(len(L))
    #print (L)
    friendship = []
    i = 0
    while True:
        line2 = g.readline()
        #print(line2.strip())
        #friendship.append(line2.strip())
        if i % 3 == 0 :
                friendship.append(line2.strip())
        i += 1
        if not line2: break
        #print(friendship)
        #print(type(friendship))
        friendship = list(set(friendship))

    print(friendship)
    f.close()
    g.close()
    #return L

'''
        if line2 not in friendship:
            #print(line2.strip())
            friendship.append(line2.strip())
'''
get_friendship_data()


def main():
    return 0