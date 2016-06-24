f = open('sm_friend.txt')

for line in f:
    line = line[0:-1]
    print(type(line))
print(type(f))

'''
def read():
    f = open('sm_friend.txt')
    print(type(f))

    for line in f:
        line = line[0:-1]
        print(type(line))
'''