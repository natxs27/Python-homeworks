def iter_even():
    i = 0
    while True:
        yield i*2
        i += 1

def iter_odd():
    i = 1
    while True:
        yield i
        i += 2

def iter_sqr():
    k=2
    i = 0
    while True:
        yield k**i
        i = 1+i
