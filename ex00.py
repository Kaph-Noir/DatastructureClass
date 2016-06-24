f = open('sm_friend.txt')

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnext):
        self.next = newnext


def main():
    list = []
    for line in f:
        if line.strip():
            line = line[0:-1]
            a= Node(line)
    print(a)

main()

'''
temp = Node(93)
a = temp.getData()
b = temp.setNext(5)
c = temp.getNext()
for i in range(2):
    print(temp)
'''