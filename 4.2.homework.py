L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse_range(a, b, c):
    for i in range(6):
        while b < c:
            a[b], a[c] = a[c], a[b]
            b = b + 1
            c = c - 1
    print(L)

reverse_range(L, 3, 6)
