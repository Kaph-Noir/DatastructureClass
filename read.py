f = open('sm_user.txt', 'r')

h = open('sm_word.txt')

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

def get_user_data():
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
    return L

def get_friend_data():
    g = open('sm_friend.txt', 'r')
    count = 0
    for line in g:
        line = line[0:-1]
        count += 1
    count +=1
    g.close()
    return count

"""
    for lines in g:
        lines = g.readlines()
        lines = list(map(lambda s: s.strip(), lines))


        print(lines)
    print (count//3)
"""

    #return 0
    # lines = g.readline()
    # lines = list(map(lambda s: s.strip(), lines))
    # print (lines)


get_friend_data()

def read_data_files():
    L = get_user_data()
    print("Total Users : ", end='');print (len(L))

    M = get_friend_data()
    print("Total Friendship Records : ", end='');print(len(L))