def hash(str):
    m = 0
    for c in str:
        m = m +ord(c)
    return m %100

def main():
    print(hash('ahis'))

main()
