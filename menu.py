def statistics():
    return 0

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

number = int(input("Select Menu:"))
print(number)

if number == 0:
    read()
elif number == 1:
    statistics()