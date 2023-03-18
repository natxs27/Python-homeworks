a = list()
for x in range(1,41):
    if x % 35 == 0:
        print(x, "is divided by 5 and 7.")
    elif x % 5 == 0:
         print(x, "is divided by 5.")
    elif x % 7 == 0:
        print(x, "is divided by 7.")
    elif x == 13:
        pass
    else:
        a.append(x)

a = str(a)
print("Numbers", a, "are not important.")

b = list()
x = 1
while x < 40:
    if x % 35 == 0:
        print(x, "is divided by 5 and 7.")
        x += 1
    elif x % 5 == 0:
        print(x, "is divided by 5.")
        x += 1
    elif x % 7 == 0:
        print(x, "is divided by 7.")
        x += 1
    elif x == 13:
        x += 1
    else:
        b.append(x)
        x += 1

b = str(b)
print("Numbers", b, "are not important.")
