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

#
#
#

'''function part'''
#
# 0. Read data files 기능 구현
#

# Print data
def read_data_files():
    L = get_user_data()
    print("Total Users : ", end='');print (len(L))
    C = get_friend_data()
    print("Total Friendship Records : ", end='');print(C//3)
    W = get_word_data()
    print("Total Tweets : ", end='');print (W//4)

# user.txt 다루기 + Total User 구하기
def get_user_data():
    f = open('sm_user.txt', 'r')
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

# friend.txt 다루기 + Total Friendship Records 구하기
def get_friend_data():
    g = open('sm_friend.txt', 'r')
    count = 0
    for line in g:
        line = line[0:-1]
        count += 1
    count +=1
    g.close()
    return count

# word.txt 다루기 + Total Tweets 구하기
def get_word_data():
    h = open('sm_word.txt')
    count = 0
    for line in h:
        line = line[0:-1]
        count += 1
    count += 1
    h.close()
    return count

#
#
#

#
# 1. Display Statistics 기능 구현
#

def get_statistics():
    return 0


#
#
#

#
# Display Interfaces
#

# Menu
print("=== Interface ===")
print("0. Read data files")
print("1. display statistics")
print("2. Top 5 most tweeted words")
print("3. Top 5 most tweeted users")
print("4. Find users who tweeted a word")
print("5. Find all people who are friends of the above users")
print("6. Delete all mentions of a word")
print("7. Delete all users who mentioned a word")
print("8. Find strongly connected components")
print("9. Find shortest path from a given user")
print("99. Quit")

# Button
number = int(input("Select Menu:"))
print("You pressed", end =' ');print(number)


# Conditions
if number == 0:
    read_data_files()
elif number == 1:
    get_statistics()

#
#
#