f = open('sm_friend.txt')
print (f)

node =''
for line in f:
    if line.strip():
        line = line[0:-1]
        node += line
        print(node)


'''
def read():
    f = open('sm_friend.txt')
    print(type(f))

    for line in f:
        line = line[0:-1]
        print(type(line))
'''