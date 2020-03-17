b = 0
for x in range(1,101):
    if not (x%3):
        b = 1
    if not (x%5):
        b = b + 2
    if b:
        if (b != 2):
            print("Crackle",end = "")
        if b > 1:
            print("Pop",end = "")
        print("")
        b = 0
    else:
        print(x)
