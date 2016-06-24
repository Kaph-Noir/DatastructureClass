f = open('sm_friend.txt')

list = []
for line in f:
    if line.strip():
        line = line[0:-1]
        list.append(line)
print(list)

'''
def read():
    f = open('sm_friend.txt')
    print(type(f))

    for line in f:
        line = line[0:-1]
        print(type(line))
'''