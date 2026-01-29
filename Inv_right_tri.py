size = int(input("Enter size of pattern: "))
for i in range (size, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()