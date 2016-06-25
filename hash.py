import hashlib

#
# file 호출부
#

f = open('sm_user.txt', 'r')
g = open('sm_friend.txt', 'r')
h = open('sm_word.txt', 'r')

def get_data():
    # user.txt 다루기
    i=0
    list1=[]
    L=[]
    while True:
        line = f.readline()
        if i % 4 == 0:
            if line: # 개행문자 제거
                list1.append(line.strip())
        i += 1
        if not line: break

    list1.sort()
    print (list1)

    #print(a)

    # friend.txt 다루기
    friendship = []
    friend = []
    i = 0
    while True:
        line1 = g.readline()
        #print(line2.strip())
        #friendship.append(line2.strip())
        if i % 3 == 0 :
            if line1:
                friendship.append(line1.strip())
                #if friendship[i] in list1:

        if not line1: break
        #print(type(friendship))

        if i % 3 == 1 :
            if line1:
                friend.append(line1.strip())
        i += 1
    #tmp1 = friendship
    tmp2 = friend

    # list 내부 중복 제거
    #friendship = list(set(friendship))

    #friendship.sort()
    print(len(friendship))
    print(len(friend))

    #print(friend)


    f.close()
    g.close()
    #return L



get_data()


def get_hash(list1, list2):
    hash = {k:v for k, v in zip(keys, vals)}
    return hash

keys = ['a', 'b', 'c']
vals = [1, 2, 3]

hash = {k:v for k, v in zip(keys, vals)}
print(type(hash))

print(hash)
'''
def hash(list):
    list = 0
    for k in list.keys():
        print (list[k])


def main():
    a = [1,2,3]
    print(hash(a))

main()
'''