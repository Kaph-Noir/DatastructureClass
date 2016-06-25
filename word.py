#
# file 호출부
#

f = open('sm_user.txt', 'r')
g = open('sm_friend.txt', 'r')
h = open('word.txt', 'r')

# word.txt 다루기
def get_word():
    i=0
    list1=[]
    # tweeted word 추출
    while True:
        line = h.readline()
        #print(line)
        if i % 4 == 2:
            if line: # 개행문자 제거
                list1.append(line.strip())
        i += 1
        if not line: break

    list1.sort()
    #print(len(list1))
    # print (list1)
    t = hash(list1)
    return t
'''
def get_who():
    j = 0
    list2 = []
    # user who tweeted 추출
    while True:
        line1 = h.readline()
        #print(line1)
        if j % 4 == 0:
            if line1:  # 개행문자 제거
                list2.append(line1.strip())
        j += 1
        if not line1: break

    #list1.sort()
    #print(len(list1))
    #print(list2)
    return list2
'''

def hash(list):
    m = 0
    for i in range(len(list)):
        for c in list[i]:
            m = m+ord(list[i])
    return m


def main():
    a = get_word()
    #b = get_who()

    print(a)
    #print(b)

main()


f.close()
g.close()
h.close()